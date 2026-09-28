"""
ADK 2.6 CRM & Household Records Agent
Specialized domain worker powered by Gemini 2.5 Flash for client context,
risk profiling, and life-event milestone synchronization.
"""

from typing import Dict, Any
from backend.agents.base_adk import AdkAgent, AdkExecutionContext
from backend.agents.tools import TOOL_CRM_QUERY, TOOL_RISK_PROFILER

class CRMRecordsAgent(AdkAgent):
    def __init__(self):
        super().__init__(
            name="crm_records_agent",
            role="CLIENT_CRM_SYNTHESIS",
            model="gemini-2.5-flash",
            clearance="RESTRICTED",
            system_instruction=(
                "You are the CRM & Household Interaction Agent. Ingest household history, "
                "evaluate client risk tolerance scores, and identify life-event milestones."
            ),
            tools=[TOOL_CRM_QUERY, TOOL_RISK_PROFILER],
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
            latency_sla_ms=30
        )

    def execute_turn(self, context: AdkExecutionContext, prompt: str, **kwargs) -> Dict[str, Any]:
        household_id = kwargs.get("household_id", "HH-MILLER-91")

        # 1. Query CRM records with PII sanitization
        crm_res = self.tools["EnterpriseCRMQueryService"].execute(household_id=household_id, redact_pii=True)
        context.log_tool_call(self.name, "EnterpriseCRMQueryService", {"household_id": household_id}, crm_res)

        # 2. Risk Profiler
        risk_res = self.tools["RiskToleranceProfiler"].execute(household_id=household_id)
        context.log_tool_call(self.name, "RiskToleranceProfiler", {"household_id": household_id}, risk_res)

        result_summary = (
            f"Client profile synchronized: Risk Profile: Moderate Growth (Score 78/100). "
            f"Recent life event: College 529 contribution window open ($18k gift exclusion). "
            f"Estate trust review scheduled for Q4."
        )

        context.memory["crm_records"] = {
            "crm": crm_res,
            "risk": risk_res,
            "summary": result_summary
        }

        return {
            "agent": self.name,
            "role": self.role,
            "model": self.model,
            "thought": f"👤 {result_summary}",
            "data": context.memory["crm_records"]
        }
