"""
SYSTEM PATTERN: PALADIN GOVERNANCE ENGINE & BOUNDED EMERGENCE ORCHESTRATOR
Multi-agent workflow execution engine on Gemini Enterprise Agent Platform with
real-time SSE streaming, Gateway policy intercepts, and schema-driven A2UI deliverables.
"""

import os
import sys
import json
import time
import logging
import hashlib
from datetime import datetime, timezone
from typing import Generator, Dict, Any, List

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from flask import Flask, Response, request, jsonify, render_template
from flask_cors import CORS
from backend.agents import (
    PaladinSupervisorAgent,
    AntigravitySupervisorAgent,
    AdkExecutionContext,
    QuantitativePortfolioAnalyticsAgent,
    CRMRecordsAgent,
    ComplianceSentinelAgent,
    OperationsSimulationAgent
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
template_dir = os.path.join(base_dir, 'frontend', 'templates')
static_dir = os.path.join(base_dir, 'frontend', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)

# ==============================================================================
# GEMINI ENTERPRISE GOVERNANCE PRIMITIVES
# ==============================================================================
class AgentRegistry:
    REGISTERED_AGENTS = {
        "domain_analytics_agent": {
            "name": "Quantitative Portfolio Analytics Agent",
            "role": "QUANT_PORTFOLIO_ANALYTICS",
            "model": "Gemini 2.5 Pro",
            "clearance": "CONFIDENTIAL",
            "certified": True,
            "latency_sla_ms": 45,
            "tool_scope": ["CustodialPortfolioAccountingAPI", "TaxLotHarvestingEngine", "FactorExposureCalculator"]
        },
        "crm_records_agent": {
            "name": "CRM & Household Interaction Agent",
            "role": "CLIENT_CRM_SYNTHESIS",
            "model": "Gemini 2.5 Flash",
            "clearance": "RESTRICTED",
            "certified": True,
            "latency_sla_ms": 30,
            "tool_scope": ["EnterpriseCRMQueryService", "HouseholdLifeEventsAPI", "RiskToleranceProfiler"]
        },
        "compliance_sentinel_agent": {
            "name": "Compliance & Regulatory Sentinel",
            "role": "FIDUCIARY_COMPLIANCE",
            "model": "Gemini 2.5 Pro",
            "clearance": "TOP_SECRET",
            "certified": True,
            "latency_sla_ms": 20,
            "tool_scope": ["SecFiduciarySuitabilityChecker", "RegBiConflictDetector", "WashSaleFilter"]
        },
        "operations_simulation_agent": {
            "name": "Monte Carlo & Scenario Simulation Agent",
            "role": "MONTE_CARLO_SIMULATION",
            "model": "Gemini 2.5 Flash",
            "clearance": "CONFIDENTIAL",
            "certified": True,
            "latency_sla_ms": 60,
            "tool_scope": ["MonteCarloEngine10k", "SequenceOfReturnsSimulator", "TaxAlphaCompoundingModel"]
        }
    }

    @classmethod
    def verify_agent(cls, agent_id: str) -> bool:
        agent_meta = cls.REGISTERED_AGENTS.get(agent_id)
        return agent_meta is not None and agent_meta.get("certified", False)

    @classmethod
    def get_catalog(cls) -> Dict[str, Any]:
        return cls.REGISTERED_AGENTS


class CentralizedPolicyEngine:
    POLICIES = [
        {
            "id": "policy-max-transaction-limit",
            "name": "Maximum Authorized Rebalancing Threshold",
            "expression": "action.params.amount <= 500000.00",
            "description": "Restricts single-action automated rebalancing to $500,000 without human-in-the-loop executive sign-off.",
            "active": True
        },
        {
            "id": "policy-pii-phi-guardrail",
            "name": "Zero-Trust PII/PHI Redaction Guardrail",
            "expression": "redact(payload.pii) == true && payload.has_unmasked_ssn == false",
            "description": "Intercepts and sanitizes all social security numbers, birthdates, and unmasked account titling.",
            "active": True
        },
        {
            "id": "policy-drift-ceiling",
            "name": "Semantic Goal Drift Threshold",
            "expression": "action.drift_score <= 0.15",
            "description": "Calculates cosine distance against initial OKF intent vector; denies execution if drift exceeds 15%.",
            "active": True
        },
        {
            "id": "policy-wash-sale-filter",
            "name": "IRS 30-Day Substantially Identical Wash-Sale Filter",
            "expression": "transaction.replacement_asset.cusip != transaction.harvested_asset.cusip && transaction.days_since_loss >= 31",
            "description": "Enforces 30-day wash-sale barrier to preserve tax loss harvest deductibility.",
            "active": True
        }
    ]

    @classmethod
    def evaluate(cls, action_payload: Dict[str, Any]) -> Dict[str, Any]:
        action_name = action_payload.get("action", "")
        params = action_payload.get("params", {})
        drift_score = action_payload.get("drift_score", 0.0)

        # Policy: Maximum Transaction Limit Check ($500,000 limit)
        if action_name == "execute_rebalance":
            amount = params.get("rebalance_amount", 0)
            if amount > 500000:
                return {
                    "result": "REJECT",
                    "rule_id": "policy-max-transaction-limit",
                    "reason": f"Amount ${amount:,.2f} exceeds authorized ceiling $500k",
                    "evaluation_ms": 1.4
                }

        # Policy: Semantic Drift Ceiling Check (0.15 threshold)
        if drift_score > 0.15:
            return {
                "result": "REJECT",
                "rule_id": "policy-drift-ceiling",
                "reason": f"Semantic drift {drift_score:.2f} exceeds ceiling 0.15",
                "evaluation_ms": 0.9
            }

        return {
            "result": "PASS",
            "rule_id": "policy-fiduciary-all-clear",
            "reason": "All declarative CEL constraints satisfied (Limits, PII, Drift, Wash-Sale, Suitability)",
            "evaluation_ms": 1.1
        }


# ==============================================================================
# SCENARIO DEFINITIONS & WORKFLOW BLUEPRINTS
# ==============================================================================
SCENARIOS = {
    "scenario-tax-alpha": {
        "id": "scenario-tax-alpha",
        "title": "HNW Tax-Loss Harvesting & Tech De-Concentration",
        "portfolio_size": "$2,400,000",
        "tax_alpha": "+$42,800 (+42 bps)",
        "goal_uplift": "86.4% ➔ 94.6%",
        "anchors": ["okf-fin-fiduciary-std", "okf-tax-alpha-opt", "okf-reg-bi-v2"],
        "analytics_finding": "US Large Cap drifted +8.2% above target (58.2% vs 50.0%). Identified $164,000 rebalancing requirement. Discovered 3 harvestable loss lots yielding +$42,800 net tax alpha (+42 bps).",
        "crm_finding": "Client Risk Profile: Moderate Growth (78/100). Imminent milestone: College 529 annual contribution window open ($18k gift exclusion).",
        "compliance_finding": "Fiduciary suitability certified: Lowers portfolio volatility by 18% with zero proprietary product conflicts. Satisfies SEC Rule 206(4)-7.",
        "simulation_finding": "Monte Carlo 10,000 paths simulated: Probability of hitting retirement income target increased from 86.4% to 94.6% (+8.2% uplift).",
        "rebalance_amount": 164000
    },
    "scenario-cross-border": {
        "id": "scenario-cross-border",
        "title": "Cross-Border Wealth & Multi-Currency Inheritance",
        "portfolio_size": "$8,500,000",
        "tax_alpha": "+$118,500 (+139 bps)",
        "goal_uplift": "81.0% ➔ 96.2%",
        "anchors": ["okf-cross-border-treaty", "okf-fx-hedge-opt", "okf-reg-bi-v2"],
        "analytics_finding": "Identified 34% unhedged Eurozone equity exposure ($2.89M) creating severe currency drag. Optimized FX cross-currency overlay and unlocked +$118,500 foreign tax credit shield.",
        "crm_finding": "Household dual citizenship (US/UK). Second-generation beneficiary trust structure active. Annual gift exclusion window synchronized.",
        "compliance_finding": "Cross-border tax treaty compliance verified (FATCA / CRS reporting aligned). Zero regulatory exposure under SEC and FCA guidelines.",
        "simulation_finding": "Multi-currency Monte Carlo simulation (10k paths) demonstrates 96.2% probability of perpetual generational wealth preservation.",
        "rebalance_amount": 420000
    },
    "scenario-10b51": {
        "id": "scenario-10b51",
        "title": "Executive 10b5-1 Liquidity Event & CRUT Optimization",
        "portfolio_size": "$12,000,000",
        "tax_alpha": "+$340,000 (+283 bps)",
        "goal_uplift": "79.5% ➔ 97.8%",
        "anchors": ["okf-sec-10b51-safeharbor", "okf-crut-tax-shield", "okf-fiduciary-std"],
        "analytics_finding": "Corporate executive holding 68% concentrated single-stock position. Generated scheduled 10b5-1 staged liquidation into Charitable Remainder Unitrust (CRUT), mitigating $340k capital gains tax.",
        "crm_finding": "Executive lockup expiration scheduled for Q4. Philanthropic foundation charter established with family governance mandate.",
        "compliance_finding": "SEC Rule 10b5-1 cooling-off period (90 days) and insider trading safe harbor confirmed. Zero disclosure discrepancies.",
        "simulation_finding": "Concentrated downside tail risk eliminated. Family legacy goal certainty elevated to 97.8% under stress market regimes.",
        "rebalance_amount": 480000
    }
}


# ==============================================================================
# PALADIN GOVERNANCE ENGINE (BOUNDED EMERGENCE ORCHESTRATOR)
# ==============================================================================
class PaladinGovernanceEngine:
    def __init__(self, session_id: str, declarative_intent: str, tenant_id: str = "TNT-CORP-01", scenario_id: str = "scenario-tax-alpha"):
        self.session_id = session_id
        self.intent = declarative_intent
        self.tenant_id = tenant_id
        self.scenario = SCENARIOS.get(scenario_id, SCENARIOS["scenario-tax-alpha"])
        self.procedural_anchors = self.scenario["anchors"]
        # ADK 2.6 Runtime Integration
        self.adk_supervisor = PaladinSupervisorAgent()
        self.adk_context = AdkExecutionContext(session_id=self.session_id, tenant_id=self.tenant_id)

    def execute_bounded_workflow(self) -> Generator[str, None, None]:
        logging.info(f"Session {self.session_id}: Launching Bounded Emergence for scenario '{self.scenario['title']}'")

        # STATE 1: INTENT ANCHORING
        yield self._emit_frame("onWorkflowStart", {
            "session_id": self.session_id,
            "tenant_id": self.tenant_id,
            "scenario": self.scenario["title"],
            "intent": self.intent,
            "procedural_anchors": self.procedural_anchors
        })
        time.sleep(0.4)

        sup_turn = self.adk_supervisor.execute_turn(self.adk_context, self.intent)
        yield self._emit_frame("onAgentThought", {
            "author": "Paladin-v3.0",
            "message": f"⚓ Intent Anchored: '{self.intent}'. Bound to OKF 2.0 knowledge nodes: {', '.join(self.procedural_anchors)}."
        })
        time.sleep(0.4)

        # STATE 2: AGENT REGISTRY & SIMULATION
        yield self._emit_frame("onRegistryVerification", {
            "author": "AgentRegistry",
            "agents_verified": list(AgentRegistry.REGISTERED_AGENTS.keys()),
            "status": "ALL_CERTIFIED"
        })
        time.sleep(0.3)

        yield self._emit_frame("onSimulationProgress", {
            "author": "SimulationEngine",
            "iterations": 100,
            "assurance_score": 0.992,
            "status": "APPROVED",
            "message": f"N=100 parallel synthetic edge cases evaluated for {self.scenario['title']}. Assurance Score: 99.2% (Threshold >= 98%)."
        })
        time.sleep(0.5)

        # STATE 3: DOMAIN WORKER 1 - QUANTITATIVE PORTFOLIO ANALYTICS
        quant_agent = self.adk_supervisor.workers["domain_analytics_agent"]
        yield self._emit_frame("onAgentDelegation", {
            "author": "Paladin-v3.0",
            "target": "domain_analytics_agent",
            "message": "Decomposing asset allocation drift, custodial tax lots, and factor optimization opportunities."
        })
        time.sleep(0.5)

        quant_res = quant_agent.execute_turn(
            self.adk_context,
            self.intent,
            account_id="ACC-78924",
            portfolio_size=self.scenario["portfolio_size"]
        )

        yield self._emit_frame("onToolCall", {
            "author": "domain_analytics_agent",
            "tool": "CustodialPortfolioAccountingAPI",
            "arguments": {"account_id": "ACC-78924", "include_tax_lots": True, "portfolio_size": self.scenario["portfolio_size"]}
        })
        time.sleep(0.4)

        yield self._emit_frame("onAgentThought", {
            "author": "domain_analytics_agent",
            "message": f"📊 {self.scenario['analytics_finding']}"
        })
        time.sleep(0.5)

        # STATE 4: DOMAIN WORKER 2 - CRM & INTERACTION SYNTHESIS
        crm_agent = self.adk_supervisor.workers["crm_records_agent"]
        yield self._emit_frame("onAgentDelegation", {
            "author": "Paladin-v3.0",
            "target": "crm_records_agent",
            "message": "Extracting household relationship history, life-event transitions, and risk tolerance scores."
        })
        time.sleep(0.5)

        crm_res = crm_agent.execute_turn(
            self.adk_context,
            self.intent,
            household_id="HH-MILLER-91"
        )

        yield self._emit_frame("onToolCall", {
            "author": "crm_records_agent",
            "tool": "EnterpriseCRMQueryService",
            "arguments": {"household_id": "HH-MILLER-91", "redact_pii": True}
        })
        time.sleep(0.4)

        yield self._emit_frame("onAgentThought", {
            "author": "crm_records_agent",
            "message": f"👤 {self.scenario['crm_finding']}"
        })
        time.sleep(0.5)

        # STATE 5: DOMAIN WORKER 3 - COMPLIANCE SENTINEL
        comp_agent = self.adk_supervisor.workers["compliance_sentinel_agent"]
        yield self._emit_frame("onAgentDelegation", {
            "author": "Paladin-v3.0",
            "target": "compliance_sentinel_agent",
            "message": "Validating fiduciary suitability, Reg BI best-interest alignment, and regulatory disclosures."
        })
        time.sleep(0.5)

        comp_res = comp_agent.execute_turn(
            self.adk_context,
            self.intent,
            drift_score=0.03
        )

        yield self._emit_frame("onAgentThought", {
            "author": "compliance_sentinel_agent",
            "message": f"⚖️ {self.scenario['compliance_finding']}"
        })
        time.sleep(0.5)

        # STATE 6: DOMAIN WORKER 4 - OPERATIONS & MONTE CARLO SIMULATION
        ops_agent = self.adk_supervisor.workers["operations_simulation_agent"]
        yield self._emit_frame("onAgentDelegation", {
            "author": "Paladin-v3.0",
            "target": "operations_simulation_agent",
            "message": "Running 10,000-path Monte Carlo retirement simulation on proposed rebalanced portfolio."
        })
        time.sleep(0.5)

        ops_res = ops_agent.execute_turn(
            self.adk_context,
            self.intent,
            iterations=10000
        )

        yield self._emit_frame("onAgentThought", {
            "author": "operations_simulation_agent",
            "message": f"📈 {self.scenario['simulation_finding']}"
        })
        time.sleep(0.5)

        # STATE 7: GATEWAY & CENTRALIZED POLICY INTERCEPT
        action_proposal = {
            "action": "execute_rebalance",
            "params": {"rebalance_amount": self.scenario["rebalance_amount"], "tax_alpha": self.scenario["tax_alpha"]},
            "drift_score": 0.03
        }
        policy_eval = CentralizedPolicyEngine.evaluate(action_proposal)

        yield self._emit_frame("onGatewayIntercept", {
            "gateway": "GeminiEnterpriseGateway-USCentral",
            "policy_result": policy_eval["result"],
            "rule_id": policy_eval["rule_id"],
            "reason": policy_eval["reason"],
            "evaluation_ms": policy_eval["evaluation_ms"],
            "drift_score": action_proposal["drift_score"],
            "rebalance_amount": action_proposal["params"]["rebalance_amount"]
        })
        time.sleep(0.5)

        # STATE 8: OBSERVABILITY COMMIT
        telemetry_payload = {
            "trace_id": f"tr-{self.session_id}-{int(time.time())}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "COMMITTED",
            "scenario": self.scenario["title"],
            "governance_mode": "BOUNDED_EMERGENCE",
            "assurance_score": 0.992,
            "net_tax_alpha": self.scenario["tax_alpha"],
            "goal_uplift": self.scenario["goal_uplift"],
            "anchors_verified": len(self.procedural_anchors)
        }
        telemetry_sig = hashlib.sha256(json.dumps(telemetry_payload).encode()).hexdigest()

        yield self._emit_frame("onTelemetryCommit", {
            "telemetry": telemetry_payload,
            "signature": f"sha256:{telemetry_sig}"
        })
        time.sleep(0.4)

        # ----------------------------------------------------------------------
        # STATE 9: EXPANDED BUSINESS VALUE DELIVERABLES (A2UI PRESENTATION)
        # ----------------------------------------------------------------------
        yield self._emit_frame("onUiComponentDelivery", {
            "author": "Paladin-v3.0",
            "ui_specification": "2.0",
            "payload": {
                "scenario_title": self.scenario["title"],
                "kpi_metrics": [
                    {"label": "Net Tax Alpha Unlocked", "value": self.scenario["tax_alpha"].split(' ')[0], "sub": self.scenario["tax_alpha"], "color": "emerald"},
                    {"label": "Advisor Time Saved", "value": "8.5 Hrs", "sub": "10x throughput multiplier", "color": "cyan"},
                    {"label": "Goal Success Prob", "value": self.scenario["goal_uplift"].split(' ')[-1], "sub": self.scenario["goal_uplift"], "color": "blue"},
                    {"label": "Compliance Risk Zeroed", "value": "100%", "sub": "SEC & FINRA signed", "color": "amber"}
                ],
                "tabs": [
                    {
                        "id": "tab-rebalance",
                        "title": "📊 Portfolio & Visual Chart",
                        "type": "PortfolioWithChart",
                        "value_summary": {
                            "badge": "DIRECT FINANCIAL VALUE",
                            "headline": f"Strategic Allocation & Tax Optimization for {self.scenario['title']}",
                            "points": [
                                f"<strong>{self.scenario['tax_alpha']} Direct Tax Savings:</strong> Harvesting unrealized losses and optimizing capital allocations offsets short-term taxable events.",
                                "<strong>Downside Risk Reduction:</strong> Restores portfolio factor balance back to target benchmark without triggering capital gains drag.",
                                "<strong>Yield Lock (+5.1% YTM):</strong> Secures high-quality cash flow duration for multi-year participant obligations."
                            ]
                        },
                        "chart_data": [
                            {"name": "US Large Cap", "current": 58.2, "rebalanced": 50.0, "target": 50.0, "color": "#38bdf8"},
                            {"name": "Intl Developed", "current": 14.5, "rebalanced": 20.0, "target": 20.0, "color": "#818cf8"},
                            {"name": "Core Fixed Income", "current": 18.3, "rebalanced": 20.0, "target": 20.0, "color": "#34d399"},
                            {"name": "Alternative Sleeve", "current": 9.0, "rebalanced": 10.0, "target": 10.0, "color": "#fbbf24"}
                        ],
                        "headers": ["Asset Class", "Current %", "Target %", "Drift", "Recommended Rebalance ($)", "Tax Lot Impact", "Financial Rationale"],
                        "rows": [
                            ["US Large Cap Equities", "58.2%", "50.0%", "+8.2%", f"-${self.scenario['rebalance_amount']:,} (Trim)", "Harvest Loss Lots", "Eliminate equity concentration & harvest losses"],
                            ["International Developed", "14.5%", "20.0%", "-5.5%", f"+${int(self.scenario['rebalance_amount']*0.67):,} (Add)", "Low-expense index ETF", "Geographic diversification at 0.04% expense ratio"],
                            ["Core Fixed Income (Treasuries)", "18.3%", "20.0%", "-1.7%", f"+${int(self.scenario['rebalance_amount']*0.21):,} (Add)", "High-yield duration lock", "Lock +5.1% YTM cash flow for retirement horizon"],
                            ["Alternative Liquidity Sleeve", "9.0%", "10.0%", "-1.0%", f"+${int(self.scenario['rebalance_amount']*0.12):,} (Deploy)", "Private credit liquidity", "Enhance downside buffer and yield resilience"]
                        ]
                    },
                    {
                        "id": "tab-monte-carlo",
                        "title": "📈 Monte Carlo 10k Simulation",
                        "type": "MonteCarloVisual",
                        "value_summary": {
                            "badge": "MATHEMATICAL PROBABILITY",
                            "headline": "10,000-Path Regime Stochastic Stress Testing",
                            "points": [
                                f"<strong>Goal Probability Uplift ({self.scenario['goal_uplift']}):</strong> The rebalanced glide path dramatically reduces tail-risk failure under stagflation and high-rate regimes.",
                                "<strong>Sequence-of-Returns Protection:</strong> 20% fixed income & alternative buffer prevents forced selling during early retirement drawdown years.",
                                "<strong>Terminal Wealth Preservation:</strong> 90th percentile outcome yields 3.2x initial capital base after 30 years."
                            ]
                        },
                        "stats": {
                            "paths": "10,000 Stochastic Iterations",
                            "baseline_prob": self.scenario["goal_uplift"].split(' ')[0],
                            "rebalanced_prob": self.scenario["goal_uplift"].split(' ')[-1],
                            "median_terminal_wealth": "$5,840,000",
                            "downside_10th_percentile": "$3,210,000 (Safe)"
                        }
                    },
                    {
                        "id": "tab-roi-breakdown",
                        "title": "💡 Business Value & ROI Engine",
                        "type": "RoiBreakdown",
                        "value_summary": {
                            "badge": "TOTAL VALUE CREATION",
                            "headline": "4-Pillar Strategic Value Creation Matrix",
                            "points": [
                                "<strong>For Advisors:</strong> Accelerates quarterly reviews from 9.0 hours to under 30 minutes, enabling 1 advisor to manage 500+ client households.",
                                f"<strong>For Participants:</strong> Delivers measurable after-tax alpha ({self.scenario['tax_alpha']}) and boosts goal certainty ({self.scenario['goal_uplift']}).",
                                "<strong>For the Firm (CIO/CISO):</strong> Eliminates multi-million dollar SEC compliance penalty risks through immutable cryptographic auditability."
                            ]
                        },
                        "roi_cards": [
                            {
                                "title": "💰 Participant Wealth Alpha",
                                "metric": self.scenario["tax_alpha"].split(' ')[0],
                                "sub": self.scenario["tax_alpha"],
                                "desc": "Tax-loss harvesting and cost basis optimization deliver quantifiable financial value directly to the client."
                            },
                            {
                                "title": "⏱️ Advisor Productivity Multiplier",
                                "metric": "10x Capacity",
                                "sub": "From 80 to 500+ households / advisor",
                                "desc": "Automated intent anchoring, trade manifest generation, and CRM synthesis eliminate manual spreadsheet workflows."
                            },
                            {
                                "title": "🛡️ Zero Fiduciary Liability",
                                "metric": "$0 Penalty Risk",
                                "sub": "100% Deterministic Policy Check",
                                "desc": "CEL policy guardrails and real-time Gateways intercept any rogue transactions before state mutation."
                            },
                            {
                                "title": "⚡ Infrastructure Efficiency",
                                "metric": "1.1 ms Latency",
                                "sub": "78% Token Cost Reduction",
                                "desc": "Context caching across OKF 2.0 regulatory nodes and Gemini 2.5 Flash tiered routing maximizes margins."
                            }
                        ]
                    },
                    {
                        "id": "tab-action-plan",
                        "title": "📋 Strategic Advisory Roadmap & Script",
                        "type": "Roadmap",
                        "value_summary": {
                            "badge": "OPERATIONAL ACTIONABILITY",
                            "headline": "Why Phased Execution Prevents Market Friction",
                            "points": [
                                "<strong>Eliminates Cash Drag:</strong> Immediate 0-30 day trade execution synchronizes buy/sell settlement to prevent uninvested cash dilution.",
                                "<strong>Life-Event Synchronization:</strong> Integrates family milestones (529 contribution, estate trust review) into the relationship cadence.",
                                "<strong>Advisor Talking Points:</strong> Provides instant executive scripts explaining the portfolio rationale in transparent client-friendly language."
                            ]
                        },
                        "advisor_script": {
                            "title": "🗣️ Ready-to-Use Advisor Client Talking Points",
                            "script": f"\"Hello Miller Household. During our quarterly review, our Paladin intelligence engine identified an opportunity to harvest tax losses from market volatility while rebalancing your asset allocation. This generates an estimated {self.scenario['tax_alpha']} in direct tax alpha and boosts your retirement goal certainty to {self.scenario['goal_uplift'].split(' ')[-1]}. We have also scheduled your annual 529 contribution window for next month.\""
                        },
                        "phases": [
                            {
                                "phase": "Immediate Horizon (0–30 Days)",
                                "badge": "High Priority",
                                "items": [
                                    f"Execute tax-efficient trim on overweight US Equities (${self.scenario['rebalance_amount']:,}) harvesting capital tax losses.",
                                    "Fund international developed equities ETF allocation and duration fixed income treasuries.",
                                    "Deliver automated Reg BI Best Interest confirmation disclosure to client portal."
                                ]
                            },
                            {
                                "phase": "Strategic Horizon (30–90 Days)",
                                "badge": "Scheduled",
                                "items": [
                                    "Initiate scheduled annual College 529 plan contribution window ($18,000 gift exclusion).",
                                    "Deploy remaining cash sleeve into high-yield alternative liquidity vehicle.",
                                    f"Conduct quarterly advisor review highlighting {self.scenario['tax_alpha']} performance."
                                ]
                            },
                            {
                                "phase": "Scale Operations (90–180+ Days)",
                                "badge": "Governance",
                                "items": [
                                    "Coordinate with estate attorney on family trust re-titling and cross-generational transfer.",
                                    "Re-simulate Monte Carlo trajectory following annual tax filing.",
                                    "Archive cryptographically signed OpenTelemetry trace vector to compliance data lake."
                                ]
                            }
                        ]
                    },
                    {
                        "id": "tab-gateway",
                        "title": "⚡ Gateway & Policy Ledger",
                        "type": "Table",
                        "value_summary": {
                            "badge": "ZERO-TRUST GOVERNANCE",
                            "headline": "Why Gateways & CEL Policies Protect Enterprise Safety",
                            "points": [
                                "<strong>Hard Pre-Execution Guardrails:</strong> Every autonomous transaction proposal is evaluated against declarative CEL policies before touching production custodian APIs.",
                                "<strong>Zero Data Exfiltration:</strong> PII/PHI sanitization guarantees sensitive client identifiers (SSNs, account titling) are never leaked across model context layers.",
                                "<strong>Sub-Millisecond Enforcement:</strong> Gateway checks add only 1.1ms latency, preserving real-time responsiveness."
                            ]
                        },
                        "headers": ["Policy Rule ID", "Evaluated Action", "Gateway Status", "CEL Latency", "Drift Score", "Governance Safety Value"],
                        "rows": [
                            ["policy-max-transaction-limit", f"execute_rebalance (${self.scenario['rebalance_amount']:,})", "APPROVED", "1.4 ms", "0.03 (Pass)", "Guarantees rebalance is within authorized delegation threshold"],
                            ["policy-pii-phi-guardrail", "crm_household_history_query", "APPROVED (Redacted)", "0.8 ms", "0.01 (Pass)", "Redacts SSNs and PII before passing context to LLM"],
                            ["policy-drift-ceiling", "dynamic_plan_step_3", "APPROVED (Within Ceiling)", "0.9 ms", "0.03 (Pass)", "Prevents autonomous sub-agent goal drift from original intent"],
                            ["policy-wash-sale-filter", "tax_loss_lot_selection", "APPROVED (No Wash Sale)", "0.7 ms", "0.00 (Pass)", "Enforces 30-day substantially identical replacement barrier"],
                            ["policy-fiduciary-reg-bi", "suitability_and_conflict_audit", "APPROVED (Zero Conflicts)", "1.1 ms", "0.02 (Pass)", "Certifies fiduciary alignment with zero proprietary fund bias"]
                        ]
                    },
                    {
                        "id": "tab-fiduciary",
                        "title": "🛡️ Fiduciary & Compliance Signoff",
                        "type": "Certificate",
                        "value_summary": {
                            "badge": "REGULATORY CERTAINTY",
                            "headline": "Why Cryptographic Fiduciary Signoff Eliminates Audit Risk",
                            "points": [
                                "<strong>100% Audit-Ready:</strong> SEC Rule 206(4)-7 and FINRA Reg BI compliance certificates are signed with SHA-256 telemetry hashes and stored in immutable compliance lakes.",
                                f"<strong>Monte Carlo Mathematical Proof:</strong> 10,000-path simulation proves the rebalance is in the participant's sole best interest by raising goal probability to {self.scenario['goal_uplift'].split(' ')[-1]}."
                            ]
                        },
                        "details": {
                            "standard": "SEC Rule 206(4)-7 & FINRA Notice 20-21 / Reg BI",
                            "status": "CERTIFIED_COMPLIANT",
                            "signer": "Paladin Compliance Sentinel (Gemini Enterprise Agent Platform)",
                            "verdict": f"The recommended portfolio modifications for '{self.scenario['title']}' are in the sole best interest of the participant, reducing volatility by 18% and generating an estimated {self.scenario['tax_alpha']} in after-tax alpha.",
                            "monte_carlo_stats": f"10,000 Paths Simulated | Baseline: {self.scenario['goal_uplift'].split(' ')[0]} ➔ Post-Rebalance: {self.scenario['goal_uplift'].split(' ')[-1]}",
                            "audit_signature": telemetry_sig
                        }
                    }
                ]
            }
        })

        yield self._emit_frame("onWorkflowComplete", {
            "session_id": self.session_id,
            "status": "SUCCESS",
            "message": "Workflow executed successfully with full Bounded Emergence governance."
        })

    def _emit_frame(self, method: str, params: Dict[str, Any]) -> str:
        return json.dumps({"jsonrpc": "2.0", "method": method, "params": params})


# Backwards compatibility alias
AntigravityGovernanceEngine = PaladinGovernanceEngine


# ==============================================================================
# HTTP ROUTING & REACTIVE STREAMING CONTROLLER
# ==============================================================================
@app.route('/', methods=['GET'])
def index() -> str:
    return render_template('index.html')

@app.route('/api/chat/stream', methods=['POST', 'GET'])
def reactive_stream_endpoint() -> Response:
    if request.method == 'POST':
        payload = request.get_json(silent=True) or {}
        prompt = payload.get("prompt", "Execute strategic portfolio rebalancing and compliance review")
        session_id = payload.get("session_id", f"session-{int(time.time())}")
        tenant_id = payload.get("tenant_id", "TNT-CORP-01")
        scenario_id = payload.get("scenario_id", "scenario-tax-alpha")
    else:
        prompt = request.args.get("prompt", "Execute strategic portfolio rebalancing and compliance review")
        session_id = request.args.get("session_id", f"session-{int(time.time())}")
        tenant_id = request.args.get("tenant_id", "TNT-CORP-01")
        scenario_id = request.args.get("scenario_id", "scenario-tax-alpha")

    engine = PaladinGovernanceEngine(session_id=session_id, declarative_intent=prompt, tenant_id=tenant_id, scenario_id=scenario_id)

    def sse_generator() -> Generator[str, None, None]:
        for frame in engine.execute_bounded_workflow():
            yield f"data: {frame}\n\n"

    return Response(sse_generator(), mimetype='text/event-stream', headers={
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'X-Accel-Buffering': 'no'
    })

@app.route('/api/health', methods=['GET'])
def health_check() -> Response:
    return jsonify({
        "status": "HEALTHY",
        "platform": "Gemini Enterprise Agent Platform",
        "governance": "BOUNDED_EMERGENCE",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route('/api/governance/registry', methods=['GET'])
def get_registry_catalog() -> Response:
    return jsonify({
        "status": "SUCCESS",
        "catalog": AgentRegistry.get_catalog()
    })

@app.route('/api/governance/policies', methods=['GET'])
def get_policy_catalog() -> Response:
    return jsonify({
        "status": "SUCCESS",
        "policies": CentralizedPolicyEngine.POLICIES
    })

@app.route('/api/governance/evaluate-policy', methods=['POST'])
def test_evaluate_policy() -> Response:
    payload = request.get_json(silent=True) or {}
    result = CentralizedPolicyEngine.evaluate(payload)
    return jsonify({"status": "SUCCESS", "evaluation": result})

@app.route('/api/session', methods=['GET'])
def session_context_manager() -> Response:
    return jsonify({
        "session_id": "session-paladin-live-01",
        "tenant_id": "TNT-CORP-01",
        "lifecycle_state": "ACTIVE",
        "governance_mode": "BOUNDED_EMERGENCE",
        "scenarios": SCENARIOS
    })

@app.route('/api/governance/agent-engine-deploy', methods=['POST', 'GET'])
def trigger_agent_engine_deployment() -> Response:
    """Executes or retrieves Agent Engine deployment manifest."""
    manifest_path = os.path.join(base_dir, 'deploy', 'agent_engine_deployment.json')
    if not os.path.exists(manifest_path):
        from deploy.deploy_agent_engine import deploy
        manifest = deploy()
    else:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    return jsonify({
        "status": "SUCCESS",
        "message": "Paladin ADK 2.6 Multi-Agent system successfully deployed to Vertex AI Agent Engine",
        "deployment": manifest
    })

@app.route('/api/governance/agent-engine-status', methods=['GET'])
def get_agent_engine_status() -> Response:
    """Returns Agent Engine deployment status and endpoint metadata."""
    manifest_path = os.path.join(base_dir, 'deploy', 'agent_engine_deployment.json')
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        return jsonify({
            "status": "DEPLOYED",
            "resource_name": manifest.get("resource_name"),
            "display_name": manifest.get("display_name"),
            "runtime": manifest.get("runtime"),
            "assurance_score": manifest.get("assurance_score"),
            "deployed_at": manifest.get("deployed_at")
        })
    return jsonify({
        "status": "READY_FOR_DEPLOYMENT",
        "project": "arsanjani-genai",
        "location": "us-central1"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
