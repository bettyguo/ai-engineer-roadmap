import { useEffect, useMemo, useState } from "react";
import { ROADMAP } from "./data.generated";
import { Diagram } from "./components/Diagram";
import { TopBar } from "./components/TopBar";
import { StageSidebar } from "./components/StageSidebar";
import { ResourcePanel } from "./components/ResourcePanel";
import { PeerFooter } from "./components/PeerFooter";
import { SearchPalette } from "./components/SearchPalette";
import type { RoadmapNode, Stage } from "./types";

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
      if (h) setSelectedId(h);
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

  // Keyboard shortcuts: / opens search, Esc closes panels, t toggles theme.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLElement && /input|textarea/i.test(e.target.tagName)) return;
      if (e.key === "/") {
        e.preventDefault();
        setSearchOpen(true);
      } else if (e.key === "Escape") {
        if (searchOpen) setSearchOpen(false);
        else if (selectedId) setSelectedId(null);
      } else if (e.key === "t") {
        setTheme((t) => (t === "dark" ? "light" : "dark"));
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [searchOpen, selectedId]);

  useEffect(() => {
    document.documentElement.classList.toggle("light", theme === "light");
    document.documentElement.classList.toggle("dark", theme === "dark");
  }, [theme]);

  return (
    <div className="flex flex-col min-h-screen">
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

        <main className="flex-1 relative min-w-0">
          <Diagram
            stages={stages}
            palette={manifest.palette}
            crossStageEdges={crossStageEdges}
            focusedStageId={focusedStageId}
            selectedId={selectedId}
            onSelect={setSelectedId}
          />
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
