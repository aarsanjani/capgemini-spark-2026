"""
ADK 2.6 (Agent Development Kit) Core Specification & Agent Abstractions
Provides typed agent definitions, tool wrappers, lifecycle callbacks,
and execution context for Gemini Enterprise multi-agent systems.
"""

import time
import json
import logging
import hashlib
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')

@dataclass
class AdkExecutionContext:
    """ADK 2.6 Execution Context: Propagates tenant, session, and OKF state across agents."""
    session_id: str
    tenant_id: str
    procedural_anchors: List[str] = field(default_factory=list)
    intent_vector: str = ""
    trace_id: str = field(default_factory=lambda: f"tr-{int(time.time() * 1000)}")
    memory: Dict[str, Any] = field(default_factory=dict)
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    gateway_intercepts: List[Dict[str, Any]] = field(default_factory=list)

    @property
    def tool_call_history(self) -> List[Dict[str, Any]]:
        return self.tool_calls

    def log_tool_call(self, agent_name: str, tool_name: str, arguments: Dict[str, Any], result: Any):
        self.tool_calls.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": agent_name,
            "tool": tool_name,
            "arguments": arguments,
            "result": result
        })

    def log_gateway_intercept(self, rule_id: str, decision: str, latency_ms: float, drift_score: float):
        self.gateway_intercepts.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "rule_id": rule_id,
            "decision": decision,
            "latency_ms": latency_ms,
            "drift_score": drift_score
        })


class AdkTool:
    """ADK 2.6 Typed Tool Abstraction with execution and schema discovery."""
    def __init__(self, name: str, description: str, func: Callable, schema: Optional[Dict[str, Any]] = None):
        self.name = name
        self.description = description
        self.func = func
        self.schema = schema or {}

    def execute(self, **kwargs) -> Any:
        try:
            return self.func(**kwargs)
        except Exception as e:
            logging.error(f"Error executing ADK tool {self.name}: {e}")
            raise e

    def get_declaration(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.schema
        }


class AdkAgent:
    """ADK 2.6 Base Agent for Gemini Enterprise Platform."""
    def __init__(
        self,
        name: str,
        role: str,
        model: str,
        clearance: str,
        system_instruction: str,
        tools: Optional[List[AdkTool]] = None,
        disallow_transfer_to_parent: bool = True,
        disallow_transfer_to_peers: bool = True,
        latency_sla_ms: int = 50
    ):
        self.name = name
        self.role = role
        self.model = model
        self.clearance = clearance
        self.system_instruction = system_instruction
        self.tools: Dict[str, AdkTool] = {t.name: t for t in (tools or [])}
        self.disallow_transfer_to_parent = disallow_transfer_to_parent
        self.disallow_transfer_to_peers = disallow_transfer_to_peers
        self.latency_sla_ms = latency_sla_ms

    def register_tool(self, tool: AdkTool):
        self.tools[tool.name] = tool

    def execute_turn(self, context: AdkExecutionContext, prompt: str, **kwargs) -> Dict[str, Any]:
        """Executes a single reasoning and tool-dispatching turn for this agent."""
        raise NotImplementedError("Subclasses of AdkAgent must implement execute_turn.")

    def to_registry_manifest(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "model": self.model,
            "clearance": self.clearance,
            "certified": True,
            "latency_sla_ms": self.latency_sla_ms,
            "tool_scope": list(self.tools.keys())
        }


class AdkRunner:
    """ADK 2.6 Orchestration Runner with Gateway Intercepts & Telemetry Emitters."""
    def __init__(self, supervisor_agent: AdkAgent):
        self.supervisor = supervisor_agent
        self.session_registry: Dict[str, AdkExecutionContext] = {}

    def get_or_create_context(self, session_id: str, tenant_id: str, intent: str, anchors: List[str]) -> AdkExecutionContext:
        if session_id not in self.session_registry:
            self.session_registry[session_id] = AdkExecutionContext(
                session_id=session_id,
                tenant_id=tenant_id,
                procedural_anchors=anchors,
                intent_vector=intent
            )
        return self.session_registry[session_id]
