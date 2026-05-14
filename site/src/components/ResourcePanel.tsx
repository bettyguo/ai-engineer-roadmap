import type { RoadmapNode, Resource, Stage } from "../types";

interface Props {
  node: RoadmapNode;
  stage: Stage;
  paletteColor: string | undefined;
  onClose: () => void;
  onSelectOther: (id: string) => void;
}

const TYPE_ICON: Record<Resource["type"], string> = {
  paper: "📄",
  course: "🎓",
  repo: "⌨︎",
  book: "📚",
  video: "▶︎",
  blog: "✎",
  tool: "⚙︎",
  official: "★",
  interactive: "◐",
};

export function ResourcePanel({ node, stage, paletteColor, onClose, onSelectOther }: Props) {
  return (
    <aside
      className="w-[420px] shrink-0 border-l border-ink-900/40 bg-ink-950/95 backdrop-blur overflow-y-auto"
      style={{ borderLeftColor: paletteColor ? paletteColor + "33" : undefined }}
      role="complementary"
      aria-label={`Resources for ${node.label}`}
    >
      <div className="p-5 border-b border-ink-900/40 sticky top-0 bg-ink-950/95 backdrop-blur z-10">
        <div className="flex items-start justify-between gap-3">
          <div>
            <div
              className="font-mono text-[10px] uppercase tracking-[0.18em] opacity-80"
              style={{ color: paletteColor }}
            >
              Stage {String(stage.stageNumber).padStart(2, "0")} · {stage.title}
            </div>
            <h2 className="font-serif text-xl mt-1">{node.label}</h2>
            <div className="mt-1 text-[10px] uppercase tracking-wider opacity-70">
              {node.status}
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-ink-100 hover:text-ink-50 text-lg leading-none -mt-1"
            aria-label="Close resource panel"
          >
            ×
          </button>
        </div>
      </div>

      <div className="p-5 space-y-5">
        <section>
          <p className="text-sm leading-relaxed text-ink-50/90">{node.description}</p>
        </section>

        <section>
          <div className="text-[10px] uppercase tracking-[0.18em] text-ink-100/60 mb-1">
            Done when
          </div>
          <p className="text-sm leading-relaxed text-ink-50/90">{node.doneWhen}</p>
        </section>

        {(node.dependsOn.length > 0 || node.crossStageDependsOn.length > 0) && (
          <section>
            <div className="text-[10px] uppercase tracking-[0.18em] text-ink-100/60 mb-1">
              Depends on
            </div>
            <div className="flex flex-wrap gap-1.5">
              {[...node.dependsOn, ...node.crossStageDependsOn].map((depId) => (
                <button
                  key={depId}
                  onClick={() => onSelectOther(depId)}
                  className="font-mono text-[11px] px-2 py-0.5 rounded-sm border border-ink-900 text-ink-100 hover:bg-ink-900"
                >
                  {depId}
                </button>
              ))}
            </div>
          </section>
        )}

        <section>
          <div className="text-[10px] uppercase tracking-[0.18em] text-ink-100/60 mb-2">
            Resources ({node.resources.length}/8)
          </div>
          {node.resources.length === 0 ? (
            <div className="text-sm text-ink-100/60 italic">
              Curation pending. Contributions welcome — see CONTRIBUTING.md.
            </div>
          ) : (
            <ul className="space-y-3">
              {node.resources.map((r, i) => (
                <li
                  key={i}
                  className="border border-ink-900/60 rounded-md p-3 hover:border-ink-200/40 transition-colors"
                >
                  <a
                    href={r.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block group"
                  >
                    <div className="flex items-baseline gap-2">
                      <span className="text-base" aria-hidden>
                        {TYPE_ICON[r.type] || "•"}
                      </span>
                      <div className="font-serif text-base leading-snug group-hover:underline">
                        {r.title}
                      </div>
                    </div>
                    <div className="mt-1 text-xs text-ink-100/70">
                      {r.author && <span>{r.author}</span>}
                      {r.author && r.year && <span> · </span>}
                      {r.year && <span>{r.year}</span>}
                    </div>
                    <div className="mt-2 text-sm text-ink-50/85 leading-relaxed">
                      {r.annotation}
                    </div>
                    <div className="mt-2 flex flex-wrap gap-1.5">
                      <Tag>{r.type}</Tag>
                      <Tag>{r.difficulty}</Tag>
                      <Tag>{r.free ? "free" : "paid"}</Tag>
                    </div>
                  </a>
                </li>
              ))}
            </ul>
          )}
        </section>
      </div>
    </aside>
  );
}

function Tag({ children }: { children: React.ReactNode }) {
  return (
    <span className="font-mono text-[10px] uppercase tracking-wider px-1.5 py-0.5 rounded-sm bg-ink-900 text-ink-100/80">
      {children}
    </span>
  );
}
