"""
TEST SUITE: ANTIGRAVITY GOVERNANCE ENGINE & BOUNDED EMERGENCE PLATFORM
Verifies Agent Registry, Centralized Policy Engine, SSE Streaming, and Health Endpoints.
"""

import json
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.app import app, AgentRegistry, CentralizedPolicyEngine

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

def test_health_check_endpoint(client):
    """Verifies that the /api/health endpoint returns 200 and HEALTHY state."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "HEALTHY"
    assert data["governance"] == "BOUNDED_EMERGENCE"
    assert data["platform"] == "Gemini Enterprise Agent Platform"

def test_session_endpoint(client):
    """Verifies session context manager response."""
    response = client.get('/api/session')
    assert response.status_code == 200
    data = response.get_json()
    assert data["session_id"] == "session-antigravity-live-01"
    assert data["lifecycle_state"] == "ACTIVE"

def test_agent_registry_attestation():
    """Ensures registered agents pass and unregistered agents fail."""
    assert AgentRegistry.verify_agent("domain_analytics_agent") is True
    assert AgentRegistry.verify_agent("crm_records_agent") is True
    assert AgentRegistry.verify_agent("compliance_sentinel_agent") is True
    assert AgentRegistry.verify_agent("operations_simulation_agent") is True
    assert AgentRegistry.verify_agent("rogue_agent_99") is False

def test_centralized_policy_engine():
    """Ensures CEL policy rules enforce transaction ceilings and drift thresholds."""
    # 1. Normal safe rebalance
    pass_payload = {
        "action": "execute_rebalance",
        "params": {"rebalance_amount": 164000},
        "drift_score": 0.03
    }
    res_pass = CentralizedPolicyEngine.evaluate(pass_payload)
    assert res_pass["result"] == "PASS"

    # 2. Excessive amount violation
    fail_amount = {
        "action": "execute_rebalance",
        "params": {"rebalance_amount": 900000},
        "drift_score": 0.03
    }
    res_fail_amount = CentralizedPolicyEngine.evaluate(fail_amount)
    assert res_fail_amount["result"] == "REJECT"
    assert res_fail_amount["rule_id"] == "policy-max-transaction-limit"

    # 3. Excessive semantic drift violation
    fail_drift = {
        "action": "execute_rebalance",
        "params": {"rebalance_amount": 100000},
        "drift_score": 0.28
    }
    res_fail_drift = CentralizedPolicyEngine.evaluate(fail_drift)
    assert res_fail_drift["result"] == "REJECT"
    assert res_fail_drift["rule_id"] == "policy-drift-ceiling"

def test_index_page_delivery(client):
    """Verifies that the root page serves the UI shell."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"ANTIGRAVITY" in response.data

def test_adk_supervisor_and_worker_agents():
    """Verifies instantiation and execution of all 4 ADK 2.6 domain workers and supervisor."""
    from backend.agents import (
        AntigravitySupervisorAgent,
        AdkExecutionContext,
        QuantitativePortfolioAnalyticsAgent,
        CRMRecordsAgent,
        ComplianceSentinelAgent,
        OperationsSimulationAgent
    )

    context = AdkExecutionContext(session_id="test-session-001", tenant_id="TNT-TEST")
    supervisor = AntigravitySupervisorAgent()
    assert supervisor.role == "BOUNDED_EMERGENCE_SUPERVISOR"
    assert len(supervisor.workers) == 4

    # 1. Supervisor Intent Anchoring
    sup_res = supervisor.execute_turn(context, "Optimize portfolio asset allocation and ensure compliance")
    assert "workers_available" in sup_res
    assert len(sup_res["workers_available"]) == 4

    # 2. Quantitative Portfolio Analytics Agent
    quant = supervisor.workers["domain_analytics_agent"]
    assert isinstance(quant, QuantitativePortfolioAnalyticsAgent)
    quant_res = quant.execute_turn(context, "Analyze tax lots", account_id="ACC-78924", portfolio_size="$2,400,000")
    assert "data" in quant_res
    assert "accounting" in quant_res["data"]
    assert "tax_lots" in quant_res["data"]

    # 3. CRM Records Agent
    crm = supervisor.workers["crm_records_agent"]
    assert isinstance(crm, CRMRecordsAgent)
    crm_res = crm.execute_turn(context, "Get CRM history", household_id="HH-MILLER-91")
    assert "data" in crm_res
    assert "crm" in crm_res["data"]
    assert crm_res["data"]["risk"]["risk_score"] == 78

    # 4. Compliance Sentinel Agent
    comp = supervisor.workers["compliance_sentinel_agent"]
    assert isinstance(comp, ComplianceSentinelAgent)
    comp_res = comp.execute_turn(context, "Verify suitability and conflicts", drift_score=0.03)
    assert comp_res["data"]["verdict"] == "APPROVED_FIDUCIARY_CLEARANCE"
    assert comp_res["data"]["sec_suitability"]["fiduciary_verdict"] == "APPROVED_SOLE_BEST_INTEREST"
    assert comp_res["data"]["reg_bi"]["reg_bi_status"] == "COMPLIANT"

    # 5. Operations Simulation Agent
    ops = supervisor.workers["operations_simulation_agent"]
    assert isinstance(ops, OperationsSimulationAgent)
    ops_res = ops.execute_turn(context, "Run Monte Carlo", iterations=10000)
    assert ops_res["data"]["monte_carlo"]["iterations"] == 10000
    assert ops_res["data"]["monte_carlo"]["rebalanced_probability"] == 0.946
    assert ops_res["data"]["sequence_returns"]["forced_selling_risk"] == "ZEROED"

    # 6. Verify Context Tool Call Audit Log
    assert len(context.tool_call_history) >= 8

def test_reactive_stream_sse(client):
    """Verifies that the /api/chat/stream endpoint emits valid SSE JSON-RPC frames."""
    response = client.post('/api/chat/stream', json={
        "prompt": "Test rebalance workflow",
        "scenario_id": "scenario-tax-alpha"
    })
    assert response.status_code == 200
    assert response.mimetype == 'text/event-stream'
    data_lines = [line.decode('utf-8') for line in response.response if line.startswith(b'data: ')]
    assert len(data_lines) >= 8

    # Parse first frame
    first_frame = json.loads(data_lines[0].replace('data: ', '').strip())
    assert first_frame["method"] == "onWorkflowStart"

    # Verify component delivery frame
    methods = [json.loads(line.replace('data: ', '').strip())["method"] for line in data_lines]
    assert "onWorkflowStart" in methods
    assert "onRegistryVerification" in methods
    assert "onSimulationProgress" in methods
    assert "onAgentDelegation" in methods
    assert "onGatewayIntercept" in methods
    assert "onTelemetryCommit" in methods
    assert "onUiComponentDelivery" in methods
    assert "onWorkflowComplete" in methods

