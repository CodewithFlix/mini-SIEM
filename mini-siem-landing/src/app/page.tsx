import { Github, Shield, Terminal, Activity, Search, Siren, CheckCircle2 } from "lucide-react";

const repoUrl = "https://github.com/CodewithFlix/mini-SIEM";

function Pill({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-full border border-white/15 bg-white/5 px-3 py-1 text-xs text-white/80">
      {children}
    </span>
  );
}

function Feature({
  icon,
  title,
  desc,
}: {
  icon: React.ReactNode;
  title: string;
  desc: string;
}) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6 shadow-sm">
      <div className="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-xl border border-white/15 bg-black/30">
        {icon}
      </div>
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="mt-2 text-sm leading-6 text-white/70">{desc}</p>
    </div>
  );
}

function Step({ n, title, code }: { n: string; title: string; code: string }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <div className="flex items-center gap-3">
        <span className="inline-flex h-7 w-7 items-center justify-center rounded-full border border-white/15 bg-black/30 text-xs text-white/80">
          {n}
        </span>
        <h4 className="font-semibold">{title}</h4>
      </div>
      <pre className="mt-4 overflow-x-auto rounded-xl border border-white/10 bg-black/50 p-4 text-xs text-white/80">
        <code>{code}</code>
      </pre>
    </div>
  );
}

export default function Home() {
  return (
    <main>
      {/* Background */}
      <div className="pointer-events-none fixed inset-0 -z-10">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,rgba(56,189,248,0.12),transparent_40%),radial-gradient(circle_at_80%_30%,rgba(168,85,247,0.10),transparent_45%),radial-gradient(circle_at_50%_80%,rgba(34,197,94,0.08),transparent_45%)]" />
        <div className="absolute inset-0 bg-[linear-gradient(to_bottom,rgba(255,255,255,0.06),transparent_30%)]" />
      </div>

      {/* Header */}
      <header className="mx-auto flex max-w-6xl items-center justify-between px-6 py-6">
        <div className="flex items-center gap-2">
          <div className="inline-flex h-9 w-9 items-center justify-center rounded-xl border border-white/15 bg-white/5">
            <Shield className="h-5 w-5" />
          </div>
          <div className="leading-tight">
            <div className="font-semibold">Mini-SIEM</div>
            <div className="text-xs text-white/60">SOC-style monitoring</div>
          </div>
        </div>

        <a
          href={repoUrl}
          target="_blank"
          rel="noreferrer"
          className="inline-flex items-center gap-2 rounded-xl border border-white/15 bg-white/5 px-4 py-2 text-sm text-white/90 hover:bg-white/10"
        >
          <Github className="h-4 w-4" />
          View on GitHub
        </a>
      </header>

      {/* Hero */}
      <section className="mx-auto max-w-6xl px-6 py-14">
        <div className="max-w-3xl">
          <div className="mb-4 flex flex-wrap gap-2">
            <Pill>Python</Pill>
            <Pill>Streamlit</Pill>
            <Pill>SQLite</Pill>
            <Pill>Detection Rules</Pill>
            <Pill>Incident Response</Pill>
          </div>

          <h1 className="text-4xl font-black leading-tight tracking-tight sm:text-5xl">
            A lightweight SIEM you can understand, run, and improve.
          </h1>

          <p className="mt-5 text-base leading-7 text-white/75 sm:text-lg">
            Mini-SIEM is a hands-on cybersecurity project that turns raw security logs into
            structured events, detects suspicious patterns, generates alerts, and supports a
            simple incident workflow — all in a SOC-style dashboard.
          </p>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <a
              href={repoUrl}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center justify-center gap-2 rounded-xl bg-white px-5 py-3 text-sm font-semibold text-black hover:bg-white/90"
            >
              <Terminal className="h-4 w-4" />
              Open Repository
            </a>

            <a
              href="#run"
              className="inline-flex items-center justify-center gap-2 rounded-xl border border-white/15 bg-white/5 px-5 py-3 text-sm font-semibold text-white/90 hover:bg-white/10"
            >
              <Activity className="h-4 w-4" />
              How to Run
            </a>
          </div>
        </div>

        {/* Mini preview card */}
        <div className="mt-10 rounded-2xl border border-white/10 bg-white/5 p-6">
          <div className="flex flex-wrap items-center gap-3 text-sm text-white/80">
            <span className="inline-flex items-center gap-2">
              <Search className="h-4 w-4" /> Audit Logs Search
            </span>
            <span className="inline-flex items-center gap-2">
              <Siren className="h-4 w-4" /> Alerts Queue
            </span>
            <span className="inline-flex items-center gap-2">
              <CheckCircle2 className="h-4 w-4" /> Open/Resolved Incidents
            </span>
          </div>
          <p className="mt-3 text-sm text-white/65">
            Built to explain SIEM fundamentals clearly: ingestion → normalization → rules →
            alerts → investigation.
          </p>
        </div>
      </section>

      {/* Features */}
      <section className="mx-auto max-w-6xl px-6 py-10">
        <h2 className="text-2xl font-bold">What it includes</h2>
        <p className="mt-2 text-sm text-white/70">
          Core SIEM building blocks, simplified — but real.
        </p>

        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <Feature
            icon={<Terminal className="h-5 w-5" />}
            title="Log Ingestion"
            desc="Reads auth-style logs and processes them into a consistent, searchable dataset."
          />
          <Feature
            icon={<Activity className="h-5 w-5" />}
            title="Normalization"
            desc="Converts raw logs into structured events (timestamp, user, IP, type, severity)."
          />
          <Feature
            icon={<Siren className="h-5 w-5" />}
            title="Detection Rules"
            desc="Rule-based detections (e.g., SSH brute force, sudo failures) with basic correlation."
          />
          <Feature
            icon={<Search className="h-5 w-5" />}
            title="Audit Log Search"
            desc="Search/filter logs by keyword, severity, user, IP, and event type — SOC style."
          />
          <Feature
            icon={<CheckCircle2 className="h-5 w-5" />}
            title="Incident Workflow"
            desc="Manage alerts with open/resolved status and analyst notes for investigation."
          />
          <Feature
            icon={<Shield className="h-5 w-5" />}
            title="Portfolio-ready"
            desc="Clean structure, simple setup, and easy roadmap for advanced improvements."
          />
        </div>
      </section>

      {/* How to run */}
      <section id="run" className="mx-auto max-w-6xl px-6 py-12">
        <h2 className="text-2xl font-bold">Run it locally</h2>
        <p className="mt-2 text-sm text-white/70">
          Quick start commands (macOS friendly).
        </p>

        <div className="mt-6 grid gap-4 lg:grid-cols-3">
          <Step
            n="1"
            title="Clone"
            code={`git clone ${repoUrl}
cd mini-SIEM`}
          />
          <Step
            n="2"
            title="Install"
            code={`python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt`}
          />
          <Step
            n="3"
            title="Ingest + Run UI"
            code={`python main.py --log samples/auth.log
streamlit run app.py`}
          />
        </div>
      </section>

      {/* Footer */}
      <footer className="mx-auto max-w-6xl px-6 py-10">
        <div className="rounded-2xl border border-white/10 bg-white/5 p-6 text-sm text-white/70">
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <div className="font-semibold text-white">Mini-SIEM</div>
              <div className="text-white/70">Built for learning detection & SOC workflows.</div>
            </div>
            <a
              href={repoUrl}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded-xl border border-white/15 bg-white/5 px-4 py-2 text-white/90 hover:bg-white/10"
            >
              <Github className="h-4 w-4" />
              GitHub Repo
            </a>
          </div>
        </div>
      </footer>
    </main>
  );
}
