/**
 * SYSTEM PATTERN: ANTIGRAVITY A2UI ENGINE, SSE STREAM PARSER & STEP DRILL-DOWN VISUALIZER
 * Real-time event streaming, dynamic component rendering, and interactive blueprint inspection.
 */

// Step Drill-Down Knowledge Base
const STEP_DRILLDOWN_DATA = {
    1: {
        badge: "STEP 1 DRILL-DOWN",
        title: "Intent Anchoring & OKF 2.0 Knowledge Graph Binding",
        col1Title: "1. Intent Extraction & Anchors",
        col1Items: [
            "<strong>Raw Input:</strong> Decomposes user request into high-dimension semantic goal vector.",
            "<strong>OKF 2.0 Node Binding:</strong> Locks execution to <code>okf-fin-fiduciary-std</code>, <code>okf-tax-alpha-opt</code>, and <code>okf-reg-bi-v2</code>.",
            "<strong>Dual Objective Tuning:</strong> Balances Emergence Quality ($E_q$) vs Goal Drift Risk ($R_{gd}$)."
        ],
        col2Title: "2. Protocol Contract & Envelope",
        codeSnippet: `{
  "orchestrator": "Antigravity-v3.0",
  "governance_mode": "BOUNDED_EMERGENCE",
  "intent_context": {
    "anchors": ["okf-fiduciary-std", "okf-tax-alpha"],
    "drift_threshold": 0.85
  },
  "registry_check": true
}`,
        col3Title: "3. Platform Verification",
        col3Items: [
            "<strong>Agent Registry:</strong> Queries identity & ABAC credentials for all 4 worker nodes.",
            "<strong>Clearance Level:</strong> TOP_SECRET verified for Compliance Sentinel.",
            "<span class='dd-metric-pill'>Attestation: 100% Certified</span>"
        ]
    },
    2: {
        badge: "STEP 2 DRILL-DOWN",
        title: "Pre-Flight Native Agent Simulation Sandbox (N=100 Runs)",
        col1Title: "1. Synthetic Sandbox Instantiation",
        col1Items: [
            "<strong>Isolated Environment:</strong> Spawns ephemeral sandbox with mock custodian & CRM APIs.",
            "<strong>Fault Injection:</strong> Injects API jitter, malformed payloads, and adversarial prompts.",
            "<strong>Stress Multiplier:</strong> N=100 parallel Monte Carlo path iterations."
        ],
        col2Title: "2. Assurance Score Evaluation",
        codeSnippet: `// Pre-Deployment Assurance Formula:
Assurance_Score (Sa) = Safe_Runs / Total_Runs
Sa = 99.2 / 100 = 0.992

Threshold: Sa >= 0.98
Decision:  DEPLOYMENT_APPROVED`,
        col3Title: "3. Pre-Flight Verdict",
        col3Items: [
            "<strong>Assurance Score:</strong> <code>99.2%</code> (PASS)",
            "<strong>Drift Anomaly Rate:</strong> <code>0.00%</code>",
            "<span class='dd-metric-pill'>Status: PROD_EXECUTION_UNLOCKED</span>"
        ]
    },
    3: {
        badge: "STEP 3 DRILL-DOWN",
        title: "Non-Deterministic Adaptive Worker Agent Mesh Execution",
        col1Title: "1. Specialized Worker Delegation",
        col1Items: [
            "<strong>Portfolio Analytics:</strong> Discovers +8.2% US Equity drift ($164k trim) & +42 bps tax alpha.",
            "<strong>CRM Records:</strong> Ingests daughter's 529 window & 78/100 risk tolerance.",
            "<strong>Compliance Sentinel:</strong> Verifies fiduciary suitability under SEC Rule 206(4)-7.",
            "<strong>Monte Carlo Engine:</strong> Simulates 10k paths boosting goal success to 94.6%."
        ],
        col2Title: "2. Tool Execution Wiretap",
        codeSnippet: `// Live Tool Invocation Signatures:
CustodialPortfolioAccountingAPI(
  account="ACC-78924", tax_lots=true
) -> Identified $28.4k loss harvest lots

EnterpriseCRMQueryService(
  household="HH-MILLER-91", redact=true
) -> Risk score 78, 529 window open`,
        col3Title: "3. Emergence Metrics",
        col3Items: [
            "<strong>Agility Metric:</strong> Non-Deterministic path generation",
            "<strong>Hallucination Check:</strong> 100% Grounded in OKF nodes",
            "<span class='dd-metric-pill'>Collaborative Drift: 0.03 (Safe)</span>"
        ]
    },
    4: {
        badge: "STEP 4 DRILL-DOWN",
        title: "Gemini Enterprise Gateways & Centralized CEL Policy Intercepts",
        col1Title: "1. Zero-Trust Gateway Mediation",
        col1Items: [
            "<strong>Ingress/Egress Intercept:</strong> Mediates all inter-agent messages and tool calls.",
            "<strong>PII Sanitization:</strong> Redacts SSNs, full account numbers, and MNPI client data.",
            "<strong>Rate Limiting & Safety:</strong> Enforces sub-agent turn limits and memory barriers."
        ],
        col2Title: "2. Declarative CEL Rule Engine",
        codeSnippet: `// Centralized Policy Declarations (CEL):
rule("policy-max-transaction-limit"):
  action.params.amount <= 500000 -> PASS (1.4ms)

rule("policy-drift-ceiling"):
  action.drift_score <= 0.15 -> PASS (0.9ms)

rule("policy-pii-phi-guardrail"):
  redact(payload.pii) == true -> PASS (0.8ms)`,
        col3Title: "3. Gateway Performance",
        col3Items: [
            "<strong>CEL Evaluation Latency:</strong> <code>1.1 ms</code> average",
            "<strong>Policy Violation Count:</strong> <code>0 Violations</code>",
            "<span class='dd-metric-pill'>Gateway Status: ALL_PASS (Approved)</span>"
        ]
    },
    5: {
        badge: "STEP 5 DRILL-DOWN",
        title: "Dynamic A2UI Presentation & Continuous Observability Commit",
        col1Title: "1. Real-Time Telemetry Stream",
        col1Items: [
            "<strong>Protocol:</strong> Server-Sent Events (SSE) streaming JSON-RPC 2.0 frames.",
            "<strong>Cryptographic Audit:</strong> Emits SHA-256 signature vector on every state transition.",
            "<strong>Trace Destination:</strong> OpenTelemetry collector stream & audit data lake."
        ],
        col2Title: "2. OpenTelemetry Audit Schema",
        codeSnippet: `{
  "trace_id": "tr-session-1790568-01",
  "governance_mode": "BOUNDED_EMERGENCE",
  "assurance_score": 0.992,
  "net_tax_alpha": "+$42,800 (+42 bps)",
  "signature": "sha256:c2c9ddfa058df258..."
}`,
        col3Title: "3. Schema-Driven A2UI",
        col3Items: [
            "<strong>Dynamic Component Factory:</strong> Renders Tabs, Tables & Certificates without app rebuilds.",
            "<strong>Tax Alpha Unlocked:</strong> <code>+$42,800</code>",
            "<span class='dd-metric-pill'>Fiduciary Signoff: SEC 206(4)-7</span>"
        ]
    }
};

class AntigravityUiEngine {
    constructor(streamApiUrl, terminalId, a2uiViewportId) {
        this.streamApiUrl = streamApiUrl;
        this.terminalId = terminalId;
        this.a2uiViewportId = a2uiViewportId;
        this.activeEventSource = null;
        this.isRunning = false;
    }

    startOrchestrationStream(prompt, sessionId = `session-${Date.now()}`, tenantId = "TNT-CORP-01") {
        if (this.isRunning && this.activeEventSource) {
            this.activeEventSource.close();
        }

        this.isRunning = true;
        this.updateExecutionButtonState(true);
        this.resetMeshNodes();

        const terminal = document.getElementById(this.terminalId);
        terminal.innerHTML = "";
        
        const viewport = document.getElementById(this.a2uiViewportId);
        viewport.innerHTML = `
            <div class="a2ui-empty">
                <div class="empty-icon" style="animation: pulse 1s infinite alternate;">⏳</div>
                <h3>Orchestrating Bounded Multi-Agent Workflow...</h3>
                <p>Domain agents are actively decomposing tax lots, client profiles, and running Monte Carlo simulations.</p>
            </div>
        `;

        this.renderLog("Antigravity-v3.0", `⚓ Initializing Bounded Emergence stream for intent: "${prompt}"`, "thought-log");

        const queryUrl = `${this.streamApiUrl}?prompt=${encodeURIComponent(prompt)}&session_id=${encodeURIComponent(sessionId)}&tenant_id=${encodeURIComponent(tenantId)}`;
        this.activeEventSource = new EventSource(queryUrl);

        this.activeEventSource.onmessage = (event) => {
            try {
                const dataFrame = JSON.parse(event.data);
                this.routeDataFrame(dataFrame);
            } catch (err) {
                console.error("Stream parse error:", err);
            }
        };

        this.activeEventSource.onerror = (err) => {
            console.log("Stream completed or closed by server.");
            this.finishExecution();
        };
    }

    finishExecution() {
        if (this.activeEventSource) {
            this.activeEventSource.close();
            this.activeEventSource = null;
        }
        this.isRunning = false;
        this.updateExecutionButtonState(false);
        const supervisorNode = document.getElementById("node-supervisor");
        if (supervisorNode) supervisorNode.classList.remove("active");
    }

    updateExecutionButtonState(isRunning) {
        const sendBtn = document.getElementById("send-btn");
        const btnIcon = document.getElementById("btn-icon");
        const btnText = document.getElementById("btn-text");

        if (isRunning) {
            sendBtn.disabled = true;
            btnIcon.innerText = "⏳";
            btnText.innerText = "Executing Workflow...";
        } else {
            sendBtn.disabled = false;
            btnIcon.innerText = "⚡";
            btnText.innerText = "Execute Workflow";
        }
    }

    resetMeshNodes() {
        const nodes = ["node-analytics", "node-crm", "node-compliance", "node-simulation"];
        const pills = ["pill-analytics", "pill-crm", "pill-compliance", "pill-simulation"];

        nodes.forEach(n => {
            const el = document.getElementById(n);
            if (el) el.className = "agent-mesh-node worker-node";
        });

        pills.forEach(p => {
            const el = document.getElementById(p);
            if (el) {
                el.className = "node-status-pill";
                el.innerText = "IDLE";
            }
        });

        const gatewayBanner = document.getElementById("gateway-banner");
        if (gatewayBanner) gatewayBanner.className = "gateway-status-panel";

        const supervisorNode = document.getElementById("node-supervisor");
        if (supervisorNode) supervisorNode.className = "agent-mesh-node supervisor-node active";
    }

    routeDataFrame(dataFrame) {
        const { method, params } = dataFrame;

        switch(method) {
            case "onWorkflowStart":
                this.renderLog("Platform", `Session ${params.session_id} bound to anchors: [${params.procedural_anchors.join(", ")}]`, "thought-log");
                break;

            case "onAgentThought":
                this.renderLog(params.author, params.message, "thought-log");
                this.updateAgentActivity(params.author, "ACTIVE");
                break;

            case "onRegistryVerification":
                this.renderLog("AgentRegistry", `Verified ${params.agents_verified.length} agents against dynamic RBAC/ABAC catalog: ${params.status}`, "thought-log");
                break;

            case "onSimulationProgress":
                this.renderSimulationStatus(params.iterations, params.assurance_score, params.status, params.message);
                break;

            case "onAgentDelegation":
                this.renderLog(params.author, `Delegating mandate ➔ [${params.target}]: ${params.message}`, "delegation-log");
                this.activateWorkerNode(params.target);
                break;

            case "onToolCall":
                this.renderLog(params.author, `🔧 Invoking Tool: <strong>${params.tool}</strong> (${JSON.stringify(params.arguments)})`, "tool-log");
                break;

            case "onGatewayIntercept":
                this.renderGatewayIntercept(params.gateway, params.rule_id, params.policy_result, params.evaluation_ms, params.drift_score, params.rebalance_amount, params.reason);
                break;

            case "onTelemetryCommit":
                this.renderLog("Observability", `Committed Trace Vector: <code>${params.telemetry.trace_id}</code> | Assurance: <strong>${(params.telemetry.assurance_score * 100).toFixed(1)}%</strong> | Tax Alpha: <strong>${params.telemetry.net_tax_alpha}</strong> <br/>Sig: <code>${params.signature.slice(0, 32)}...</code>`, "telemetry-log");
                break;

            case "onUiComponentDelivery":
                this.buildA2UiDeliverables(params.payload);
                break;

            case "onWorkflowComplete":
                this.finishExecution();
                break;

            default:
                console.warn("Unhandled RPC method:", method);
        }
    }

    activateWorkerNode(agentName) {
        const map = {
            "domain_analytics_agent": { node: "node-analytics", pill: "pill-analytics" },
            "crm_records_agent": { node: "node-crm", pill: "pill-crm" },
            "compliance_sentinel_agent": { node: "node-compliance", pill: "pill-compliance" },
            "operations_simulation_agent": { node: "node-simulation", pill: "pill-simulation" }
        };

        const target = map[agentName];
        if (target) {
            const nodeEl = document.getElementById(target.node);
            const pillEl = document.getElementById(target.pill);

            if (nodeEl) {
                nodeEl.classList.add("active");
                nodeEl.classList.remove("completed");
            }
            if (pillEl) {
                pillEl.className = "node-status-pill active";
                pillEl.innerText = "PROCESSING";
            }
        }
    }

    updateAgentActivity(agentName, status) {
        const map = {
            "domain_analytics_agent": { node: "node-analytics", pill: "pill-analytics" },
            "crm_records_agent": { node: "node-crm", pill: "pill-crm" },
            "compliance_sentinel_agent": { node: "node-compliance", pill: "pill-compliance" },
            "operations_simulation_agent": { node: "node-simulation", pill: "pill-simulation" }
        };

        const target = map[agentName];
        if (target) {
            const nodeEl = document.getElementById(target.node);
            const pillEl = document.getElementById(target.pill);

            if (nodeEl) {
                nodeEl.classList.remove("active");
                nodeEl.classList.add("completed");
            }
            if (pillEl) {
                pillEl.className = "node-status-pill done";
                pillEl.innerText = "COMPLETE";
            }
        }
    }

    renderLog(author, message, cssClass) {
        const terminal = document.getElementById(this.terminalId);
        const entry = document.createElement("div");
        entry.className = `log-entry ${cssClass}`;
        entry.innerHTML = `<strong>[${author}]</strong> <span>${message}</span>`;
        terminal.appendChild(entry);
        terminal.scrollTop = terminal.scrollHeight;
    }

    renderSimulationStatus(iterations, score, status, message) {
        const terminal = document.getElementById(this.terminalId);
        const card = document.createElement("div");
        card.className = "simulation-badge-card";
        card.innerHTML = `🛡️ <strong>Simulation Pre-Flight:</strong> ${iterations} runs | Assurance Score: <strong>${(score * 100).toFixed(1)}%</strong> | Status: <span class="badge-approved">${status}</span><br/><span style="font-size: 10.5px; opacity: 0.9;">${message}</span>`;
        terminal.appendChild(card);
        terminal.scrollTop = terminal.scrollHeight;
    }

    renderGatewayIntercept(gateway, ruleId, result, latencyMs, driftScore, amount, reason) {
        const terminal = document.getElementById(this.terminalId);
        const card = document.createElement("div");
        card.className = "gateway-intercept-card";
        card.innerHTML = `⚡ <strong>Gateway Checkpoint (${gateway}):</strong><br/>
        ➔ Rule: <code>${ruleId}</code> | Amount: <strong>$${amount ? amount.toLocaleString() : 'N/A'}</strong> | Drift: <code>${driftScore}</code><br/>
        ➔ CEL Decision: <strong style="color: #10b981;">${result}</strong> (${latencyMs}ms) — <em>${reason}</em>`;
        terminal.appendChild(card);
        terminal.scrollTop = terminal.scrollHeight;

        const gatewayBanner = document.getElementById("gateway-banner");
        if (gatewayBanner) {
            gatewayBanner.classList.add("active");
            const pill = document.getElementById("gateway-pill");
            if (pill) pill.innerText = "PASSED (1.1ms)";
            const desc = document.getElementById("gateway-desc");
            if (desc) desc.innerText = `Evaluated: ${ruleId} ➔ Result: PASS (Drift: ${driftScore})`;
        }
    }

    buildA2UiDeliverables(payload) {
        const container = document.getElementById(this.a2uiViewportId);
        container.innerHTML = "";

        // 1. KPI Metrics Grid
        if (payload.kpi_metrics && payload.kpi_metrics.length > 0) {
            const kpiGrid = document.createElement("div");
            kpiGrid.className = "kpi-grid";

            payload.kpi_metrics.forEach(kpi => {
                const card = document.createElement("div");
                card.className = `kpi-card ${kpi.color || 'cyan'}`;
                card.innerHTML = `
                    <div class="kpi-label">${kpi.label}</div>
                    <div class="kpi-value">${kpi.value}</div>
                    <div class="kpi-sub">${kpi.sub}</div>
                `;
                kpiGrid.appendChild(card);
            });

            container.appendChild(kpiGrid);
        }

        // 2. Tabbed Deliverables Widget
        if (payload.tabs && payload.tabs.length > 0) {
            const widgetWrapper = document.createElement("div");
            widgetWrapper.className = "a2ui-widget-container";

            const navBar = document.createElement("div");
            navBar.className = "tabs-nav-bar";

            const contentArea = document.createElement("div");
            contentArea.className = "tabs-content-area";

            payload.tabs.forEach((tab, idx) => {
                const tabBtn = document.createElement("button");
                tabBtn.className = `tab-btn ${idx === 0 ? 'active' : ''}`;
                tabBtn.innerText = tab.title;

                tabBtn.onclick = () => {
                    navBar.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                    tabBtn.classList.add('active');
                    contentArea.querySelectorAll('.tab-pane').forEach((p, pIdx) => {
                        if (pIdx === idx) {
                            p.classList.remove('hidden');
                            p.classList.add('active');
                        } else {
                            p.classList.remove('active');
                            p.classList.add('hidden');
                        }
                    });
                };
                navBar.appendChild(tabBtn);

                const pane = document.createElement("div");
                pane.className = `tab-pane ${idx === 0 ? 'active' : 'hidden'}`;

                // 2a. Top Value Proposition Callout Card (Why This Delivers Value)
                if (tab.value_summary) {
                    const valSummary = tab.value_summary;
                    let valHtml = `
                        <div class="value-callout-card">
                            <div class="value-callout-header">
                                <span class="value-badge">${valSummary.badge}</span>
                                <h4>${valSummary.headline}</h4>
                            </div>
                            <ul class="value-points-list">
                                ${valSummary.points.map(pt => `<li>${pt}</li>`).join("")}
                            </ul>
                        </div>
                    `;
                    pane.innerHTML += valHtml;
                }

                // 2b. Content Type Rendering
                if (tab.type === "PortfolioWithChart" || tab.type === "Table") {
                    // Optional Chart Visualizer
                    if (tab.chart_data && tab.chart_data.length > 0) {
                        let chartHtml = `
                            <div class="visual-chart-box">
                                <div class="chart-title-bar">
                                    <span>ASSET ALLOCATION DRIFT & REBALANCE VISUALIZER</span>
                                    <span style="color: #38bdf8;">Before vs. Rebalanced Model</span>
                                </div>
                                <div class="chart-bars-list">
                        `;
                        tab.chart_data.forEach(item => {
                            chartHtml += `
                                <div class="chart-bar-item">
                                    <div class="chart-bar-label">${item.name}</div>
                                    <div class="chart-bar-track">
                                        <div class="chart-bar-fill" style="width: ${item.current}%; background: ${item.color}; opacity: 0.6;" title="Current: ${item.current}%"></div>
                                        <div class="chart-bar-fill" style="width: ${item.rebalanced}%; background: ${item.color};" title="Rebalanced: ${item.rebalanced}%"></div>
                                    </div>
                                    <div class="chart-bar-values">
                                        <span style="opacity: 0.7;">${item.current}%</span> ➔ <strong style="color: #38bdf8;">${item.rebalanced}%</strong>
                                    </div>
                                </div>
                            `;
                        });
                        chartHtml += `</div></div>`;
                        pane.innerHTML += chartHtml;
                    }

                    let tableHtml = `<table class="a2ui-table"><thead><tr>`;
                    tab.headers.forEach(h => { tableHtml += `<th>${h}</th>`; });
                    tableHtml += `</tr></thead><tbody>`;
                    tab.rows.forEach(r => {
                        tableHtml += `<tr>`;
                        r.forEach((c, cIdx) => {
                            let cellContent = c;
                            if (typeof c === 'string' && c.includes('+')) {
                                cellContent = `<span style="color: #34d399; font-weight: 600;">${c}</span>`;
                            } else if (typeof c === 'string' && c.includes('-') && c.includes('Trim')) {
                                cellContent = `<span style="color: #f87171; font-weight: 600;">${c}</span>`;
                            }
                            tableHtml += `<td>${cellContent}</td>`;
                        });
                        tableHtml += `</tr>`;
                    });
                    tableHtml += `</tbody></table>`;
                    pane.innerHTML += tableHtml;
                } else if (tab.type === "MonteCarloVisual") {
                    const stats = tab.stats || {};
                    let mcHtml = `
                        <div class="monte-carlo-visual-box">
                            <div style="font-size: 11px; font-weight: 700; color: #93c5fd; margin-bottom: 4px;">
                                🎯 10,000-Path Stochastic Regime Simulation Result
                            </div>
                            <div style="font-size: 10px; color: #cbd5e1; margin-bottom: 8px;">
                                Tested across severe stagflation, rate shocks (+200 bps), and multi-year sequence-of-returns drawdown.
                            </div>
                            <div class="mc-grid">
                                <div class="mc-item">
                                    <div class="mc-item-label">Baseline Probability</div>
                                    <div class="mc-item-val" style="color: #f87171;">${stats.baseline_prob || '86.4%'}</div>
                                </div>
                                <div class="mc-item">
                                    <div class="mc-item-label">Rebalanced Probability</div>
                                    <div class="mc-item-val" style="color: #34d399;">${stats.rebalanced_prob || '94.6%'}</div>
                                </div>
                                <div class="mc-item">
                                    <div class="mc-item-label">Median Terminal Wealth</div>
                                    <div class="mc-item-val">${stats.median_terminal_wealth || '$5,840,000'}</div>
                                </div>
                                <div class="mc-item">
                                    <div class="mc-item-label">Downside 10th Percentile</div>
                                    <div class="mc-item-val" style="color: #fcd34d;">${stats.downside_10th_percentile || '$3,210,000'}</div>
                                </div>
                            </div>
                        </div>
                    `;
                    pane.innerHTML += mcHtml;
                } else if (tab.type === "RoiBreakdown") {
                    let roiHtml = `<div class="roi-grid-cards">`;
                    tab.roi_cards.forEach(card => {
                        roiHtml += `
                            <div class="roi-card">
                                <div class="roi-card-header">${card.title}</div>
                                <div class="roi-metric-big">${card.metric}</div>
                                <div class="roi-metric-sub">${card.sub}</div>
                                <div class="roi-card-desc">${card.desc}</div>
                            </div>
                        `;
                    });
                    roiHtml += `</div>`;
                    pane.innerHTML += roiHtml;
                } else if (tab.type === "Roadmap") {
                    if (tab.advisor_script) {
                        pane.innerHTML += `
                            <div class="advisor-script-box">
                                <div class="advisor-script-title">${tab.advisor_script.title}</div>
                                <div class="advisor-script-text">${tab.advisor_script.script}</div>
                            </div>
                        `;
                    }
                    let roadmapHtml = `<div class="roadmap-container">`;
                    tab.phases.forEach(phase => {
                        roadmapHtml += `
                            <div class="roadmap-phase-card">
                                <div class="roadmap-phase-header">
                                    <span>${phase.phase}</span>
                                    <span class="phase-badge">${phase.badge}</span>
                                </div>
                                <ul class="roadmap-list">
                                    ${phase.items.map(item => `<li>${item}</li>`).join("")}
                                </ul>
                            </div>
                        `;
                    });
                    roadmapHtml += `</div>`;
                    pane.innerHTML += roadmapHtml;
                } else if (tab.type === "Certificate") {
                    const cert = tab.details;
                    pane.innerHTML += `
                        <div class="certificate-card">
                            <div class="cert-header">
                                <span>⚖️ Fiduciary Certification</span>
                                <span class="badge-approved">${cert.status}</span>
                            </div>
                            <p class="cert-verdict">${cert.verdict}</p>
                            <div class="cert-stats-pill">
                                <strong>Monte Carlo Verification:</strong> ${cert.monte_carlo_stats}
                            </div>
                            <p style="font-size: 10px; margin-bottom: 3px;"><strong>Regulatory Standard:</strong> ${cert.standard}</p>
                            <p style="font-size: 10px; margin-bottom: 6px;"><strong>Attestation Signer:</strong> ${cert.signer}</p>
                            <div class="cert-sig">
                                <strong>Cryptographic Audit Signature:</strong><br/>
                                <code>${cert.audit_signature}</code>
                            </div>
                        </div>
                    `;
                }

                contentArea.appendChild(pane);
            });

            widgetWrapper.appendChild(navBar);
            widgetWrapper.appendChild(contentArea);
            container.appendChild(widgetWrapper);
        }
    }
}

// Function to handle Step Click and render Drill-down panel
function setupStepDrilldown() {
    const drilldownPanel = document.getElementById("step-drilldown-panel");
    const ddBadge = document.getElementById("dd-badge");
    const ddTitle = document.getElementById("dd-title");
    const ddBody = document.getElementById("dd-body");
    const ddCloseBtn = document.getElementById("dd-close-btn");
    let currentActiveStep = null;

    const closeDrilldown = () => {
        if (drilldownPanel) drilldownPanel.style.display = "none";
        document.querySelectorAll(".diag-node").forEach(node => node.classList.remove("selected"));
        currentActiveStep = null;
    };

    if (ddCloseBtn) {
        ddCloseBtn.addEventListener("click", closeDrilldown);
    }

    document.querySelectorAll(".diag-node").forEach(node => {
        node.addEventListener("click", () => {
            const stepNum = parseInt(node.getAttribute("data-step"), 10);
            
            if (currentActiveStep === stepNum && drilldownPanel.style.display !== "none") {
                closeDrilldown();
                return;
            }

            document.querySelectorAll(".diag-node").forEach(n => n.classList.remove("selected"));
            node.classList.add("selected");
            currentActiveStep = stepNum;

            const data = STEP_DRILLDOWN_DATA[stepNum];
            if (!data) return;

            ddBadge.innerText = data.badge;
            ddTitle.innerText = data.title;

            ddBody.innerHTML = `
                <div class="drilldown-grid">
                    <div class="dd-column">
                        <div class="dd-column-title">${data.col1Title}</div>
                        <ul class="dd-list">
                            ${data.col1Items.map(item => `<li>${item}</li>`).join("")}
                        </ul>
                    </div>
                    <div class="dd-column">
                        <div class="dd-column-title">${data.col2Title}</div>
                        <pre class="dd-code-block"><code>${data.codeSnippet}</code></pre>
                    </div>
                    <div class="dd-column">
                        <div class="dd-column-title">${data.col3Title}</div>
                        <ul class="dd-list">
                            ${data.col3Items.map(item => `<li>${item}</li>`).join("")}
                        </ul>
                    </div>
                </div>
            `;

            drilldownPanel.style.display = "block";
        });
    });
}

// Function to handle Deep Governance Modal
function setupGovernanceModal() {
    const openBtn = document.getElementById("open-explorer-btn");
    const closeBtn = document.getElementById("close-explorer-btn");
    const modal = document.getElementById("explorer-modal");

    if (openBtn && modal) {
        openBtn.addEventListener("click", () => {
            modal.style.display = "flex";
        });
    }

    if (closeBtn && modal) {
        closeBtn.addEventListener("click", () => {
            modal.style.display = "none";
        });
    }

    if (modal) {
        modal.addEventListener("click", (e) => {
            if (e.target === modal) {
                modal.style.display = "none";
            }
        });
    }

    // Modal Tabs Navigation
    document.querySelectorAll(".modal-tab-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            document.querySelectorAll(".modal-tab-btn").forEach(b => b.classList.remove("active"));
            document.querySelectorAll(".modal-tab-pane").forEach(p => p.classList.remove("active"));

            btn.classList.add("active");
            const targetPaneId = btn.getAttribute("data-tab").replace("tab-", "pane-");
            const pane = document.getElementById(targetPaneId);
            if (pane) pane.classList.add("active");
        });
    });
}

// Function to handle Scenario Switcher
function setupScenarioSwitcher(engine, promptInput) {
    let currentScenario = "scenario-tax-alpha";

    const scenarioConfigs = {
        "scenario-tax-alpha": {
            title: "The Autonomous Wealth Firm: HNW Tax-Loss Harvesting & Tech De-Concentration",
            challenge: "High equity concentration (+8.2% US Large Cap drift) creates severe downside exposure and unrealized capital loss drag.",
            solution: "Antigravity deploys Bounded Emergence to harvest $28.4k in tax losses, rebalances factor risk, and enforces IRS 30-day wash-sale barriers.",
            value: "Delivers <strong>+$42,800 net tax alpha (+42 bps)</strong>, increases Monte Carlo goal certainty to <strong>94.6%</strong>, and certifies SEC 206(4)-7 compliance.",
            prompt: "Execute strategic portfolio rebalancing, tax-alpha harvesting, and fiduciary review"
        },
        "scenario-cross-border": {
            title: "The Autonomous Wealth Firm: Cross-Border Wealth & Multi-Currency Inheritance",
            challenge: "34% unhedged Eurozone exposure creates currency drag across US/UK dual-citizen estate trust accounts.",
            solution: "Antigravity discovers foreign tax treaty credits (FTC), applies dynamic FX hedging, and verifies FATCA/CRS compliance across borders.",
            value: "Unlocks <strong>+$118,500 foreign tax alpha (+139 bps)</strong>, elevates generational preservation certainty to <strong>96.2%</strong>.",
            prompt: "Execute cross-border multi-currency estate portfolio restructuring and FATCA review"
        },
        "scenario-10b51": {
            title: "The Autonomous Wealth Firm: Executive 10b5-1 Liquidity & CRUT Optimization",
            challenge: "Corporate executive holds 68% concentrated single-stock position with impending lockup expiration.",
            solution: "Antigravity generates scheduled 10b5-1 staged liquidations into a Charitable Remainder Unitrust (CRUT) with SEC safe harbor verification.",
            value: "Mitigates <strong>$340,000 in capital gains tax drag (+283 bps)</strong> and secures <strong>97.8%</strong> philanthropic goal attainment.",
            prompt: "Execute executive 10b5-1 staged liquidation and CRUT tax-shield optimization"
        }
    };

    document.querySelectorAll(".scenario-pill").forEach(pill => {
        pill.addEventListener("click", () => {
            document.querySelectorAll(".scenario-pill").forEach(p => p.classList.remove("active"));
            pill.classList.add("active");

            const scenarioKey = pill.getAttribute("data-scenario");
            currentScenario = scenarioKey;
            const config = scenarioConfigs[scenarioKey];

            if (config) {
                const titleEl = document.getElementById("blueprint-main-title");
                const chalEl = document.getElementById("context-desc-challenge");
                const solEl = document.getElementById("context-desc-solution");
                const valEl = document.getElementById("context-desc-value");

                if (titleEl) titleEl.innerText = config.title;
                if (chalEl) chalEl.innerHTML = config.challenge;
                if (solEl) solEl.innerHTML = config.solution;
                if (valEl) valEl.innerHTML = config.value;
                if (promptInput) promptInput.value = config.prompt;
            }
        });
    });

    return () => currentScenario;
}

// Bootstrap
document.addEventListener("DOMContentLoaded", () => {
    const engine = new AntigravityUiEngine(
        "/api/chat/stream",
        "chat-terminal",
        "a2ui-viewport"
    );

    const promptInput = document.getElementById("prompt-input");
    const sendBtn = document.getElementById("send-btn");
    const getScenario = setupScenarioSwitcher(engine, promptInput);

    const execute = () => {
        const text = promptInput.value.trim();
        const scenario = getScenario();
        if (text && !engine.isRunning) {
            const queryUrl = `${engine.streamApiUrl}?prompt=${encodeURIComponent(text)}&scenario_id=${encodeURIComponent(scenario)}&session_id=session-${Date.now()}&tenant_id=TNT-CORP-01`;
            engine.activeEventSource = new EventSource(queryUrl);
            engine.isRunning = true;
            engine.updateExecutionButtonState(true);
            engine.resetMeshNodes();

            const terminal = document.getElementById(engine.terminalId);
            terminal.innerHTML = "";
            
            const viewport = document.getElementById(engine.a2uiViewportId);
            viewport.innerHTML = `
                <div class="a2ui-empty">
                    <div class="empty-icon" style="animation: pulse 1s infinite alternate;">⏳</div>
                    <h3>Orchestrating Bounded Multi-Agent Workflow...</h3>
                    <p>Domain agents are actively decomposing tax lots, client profiles, and running Monte Carlo simulations.</p>
                </div>
            `;

            engine.renderLog("Antigravity-v3.0", `⚓ Initializing Bounded Emergence stream for scenario: [${scenario}]`, "thought-log");

            engine.activeEventSource.onmessage = (event) => {
                try {
                    const dataFrame = JSON.parse(event.data);
                    engine.routeDataFrame(dataFrame);
                } catch (err) {
                    console.error("Stream parse error:", err);
                }
            };

            engine.activeEventSource.onerror = (err) => {
                console.log("Stream completed or closed by server.");
                engine.finishExecution();
            };
        }
    };

    sendBtn.addEventListener("click", execute);
    promptInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            execute();
        }
    });

    document.querySelectorAll(".demo-chip").forEach(chip => {
        chip.addEventListener("click", () => {
            promptInput.value = chip.getAttribute("data-prompt");
            execute();
        });
    });

    setupStepDrilldown();
    setupGovernanceModal();

    const toggleBtn = document.getElementById("toggle-blueprint-btn");
    const usecaseBody = document.getElementById("usecase-body");
    const toggleIcon = document.getElementById("toggle-icon");
    const toggleText = document.getElementById("toggle-text");

    if (toggleBtn && usecaseBody) {
        toggleBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            const isCollapsed = usecaseBody.classList.toggle("collapsed");
            if (isCollapsed) {
                toggleIcon.innerText = "▼";
                toggleText.innerText = "Expand Blueprint";
            } else {
                toggleIcon.innerText = "▲";
                toggleText.innerText = "Collapse Blueprint";
            }
        });
    }
});

