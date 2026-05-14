import { Suspense, lazy, useEffect, useMemo, useState } from "react";
import { ROADMAP } from "./data.generated";
import { TopBar } from "./components/TopBar";
import { StageSidebar } from "./components/StageSidebar";
import { ResourcePanel } from "./components/ResourcePanel";
import { PeerFooter } from "./components/PeerFooter";
import { SearchPalette } from "./components/SearchPalette";
import type { RoadmapNode, Stage } from "./types";

// React Flow is the bulk of the bundle; load it on its own chunk so the
// first paint (TopBar + Sidebar + loader) is small and fast.
const Diagram = lazy(() =>
  import("./components/Diagram").then((m) => ({ default: m.Diagram })),
);

interface SelectedNode {
  node: RoadmapNode;
  stage: Stage;
}

function findNode(stages: Stage[], id: string): SelectedNode | null {
  for (const stage of stages) {
    const node = stage.nodes.find((n) => n.id === id);
    if (node) return { node, stage };
  }
  return null;
}

export default function App() {
  const { manifest, stages, peers, crossStageEdges } = ROADMAP;
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [focusedStageId, setFocusedStageId] = useState<string | null>(null);
  const [searchOpen, setSearchOpen] = useState(false);
  const [theme, setTheme] = useState<"dark" | "light">("dark");

  const selected = useMemo(
    () => (selectedId ? findNode(stages, selectedId) : null),
    [selectedId, stages],
  );

  // Hash-link routing: #node-id selects that node on load and on hashchange.
  useEffect(() => {
    const applyHash = () => {
      const h = window.location.hash.replace(/^#/, "");
      if (h && h !== "main") setSelectedId(h);
    };
    applyHash();
    window.addEventListener("hashchange", applyHash);
    return () => window.removeEventListener("hashchange", applyHash);
  }, []);

  useEffect(() => {
    if (selectedId) {
      const hash = `#${selectedId}`;
      if (window.location.hash !== hash) {
        history.replaceState(null, "", hash);
      }
    }
  }, [selectedId]);

  // Keyboard shortcuts: / opens search, Esc closes panels, t toggles theme,
  // ? opens a brief help dialog (handled by SearchPalette's empty hint).
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLElement && /input|textarea/i.test(e.target.tagName)) return;
      if (e.key === "/") {
        e.preventDefault();
        setSearchOpen(true);
      } else if (e.key === "Escape") {
        if (searchOpen) setSearchOpen(false);
        else if (selectedId) setSelectedId(null);
        else if (focusedStageId) setFocusedStageId(null);
      } else if (e.key === "t") {
        setTheme((t) => (t === "dark" ? "light" : "dark"));
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [searchOpen, selectedId, focusedStageId]);

  useEffect(() => {
    document.documentElement.classList.toggle("light", theme === "light");
    document.documentElement.classList.toggle("dark", theme === "dark");
  }, [theme]);

  // Announce the currently selected node to screen readers so keyboard /
  // SR users get audible feedback when they click a node or follow a
  // hash link.
  const announcement = selected
    ? `Selected node: ${selected.node.label}. Stage ${selected.stage.stageNumber}, ${selected.stage.title}. ${selected.node.resources.length} resources.`
    : "";

  return (
    <div className="flex flex-col min-h-screen">
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:left-2 focus:top-2 focus:z-50 focus:bg-ink-950 focus:text-ink-50 focus:px-3 focus:py-1.5 focus:rounded-sm focus:ring-2 focus:ring-offset-2 focus:ring-offset-ink-950 focus:ring-ink-200"
      >
        Skip to main content
      </a>
      <div className="sr-only" role="status" aria-live="polite" aria-atomic="true">
        {announcement}
      </div>

      <TopBar
        manifest={manifest}
        onSearchClick={() => setSearchOpen(true)}
        theme={theme}
        onToggleTheme={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
      />

      <div className="flex flex-1 min-h-0">
        <StageSidebar
          stages={stages}
          palette={manifest.palette}
          focusedStageId={focusedStageId}
          onFocus={(sid) => setFocusedStageId((s) => (s === sid ? null : sid))}
        />

        <main id="main" className="flex-1 relative min-w-0" aria-label="Roadmap diagram">
          <Suspense fallback={<DiagramFallback />}>
            <Diagram
              stages={stages}
              palette={manifest.palette}
              crossStageEdges={crossStageEdges}
              focusedStageId={focusedStageId}
              selectedId={selectedId}
              onSelect={setSelectedId}
            />
          </Suspense>
        </main>

        {selected && (
          <ResourcePanel
            node={selected.node}
            stage={selected.stage}
            paletteColor={manifest.palette[selected.stage.id]}
            onClose={() => setSelectedId(null)}
            onSelectOther={setSelectedId}
          />
        )}
      </div>

      <PeerFooter peers={peers} curator={manifest.curator} repo={manifest.repo} />

      {searchOpen && (
        <SearchPalette
          stages={stages}
          onClose={() => setSearchOpen(false)}
          onSelect={(id) => {
            setSelectedId(id);
            setSearchOpen(false);
          }}
        />
      )}
    </div>
  );
}

function DiagramFallback() {
  return (
    <div className="absolute inset-0 flex items-center justify-center" role="status" aria-label="Loading diagram">
      <div className="text-center space-y-3 px-6">
        <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-100/55">
          loading roadmap
        </div>
        <div className="flex items-center justify-center gap-1">
          <span className="w-1.5 h-1.5 bg-ink-100/60 rounded-full animate-pulse" />
          <span className="w-1.5 h-1.5 bg-ink-100/60 rounded-full animate-pulse [animation-delay:120ms]" />
          <span className="w-1.5 h-1.5 bg-ink-100/60 rounded-full animate-pulse [animation-delay:240ms]" />
        </div>
        <p className="text-xs text-ink-100/55 max-w-xs">
          The diagram is loading. If it stays empty, JavaScript may be disabled —
          the static markdown view in <code className="font-mono">content/</code> is the fallback.
        </p>
      </div>
    </div>
  );
}
