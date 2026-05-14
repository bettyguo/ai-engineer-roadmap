import type { Stage } from "../types";

interface Props {
  stages: Stage[];
  palette: Record<string, string>;
  focusedStageId: string | null;
  onFocus: (sid: string) => void;
}

export function StageSidebar({ stages, palette, focusedStageId, onFocus }: Props) {
  return (
    <aside className="hidden lg:flex flex-col w-[240px] shrink-0 border-r border-ink-900/60 bg-ink-950/85 overflow-y-auto">
      <div className="px-4 py-3 border-b border-ink-900/60 space-y-2">
        <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-100/55">
          Legend
        </div>
        <ul className="space-y-1.5 text-[11px] text-ink-100/85">
          <li className="flex items-center gap-2">
            <span className="inline-block w-3 h-3 rounded-sm bg-ink-200/70 shrink-0" aria-hidden />
            <span><span className="font-medium">core</span> — study this</span>
          </li>
          <li className="flex items-center gap-2">
            <span className="inline-block w-3 h-3 rounded-sm border border-ink-200/70 shrink-0" aria-hidden />
            <span><span className="font-medium">recommended</span> — if your role touches it</span>
          </li>
          <li className="flex items-center gap-2">
            <span className="inline-block w-3 h-3 rounded-sm border border-dashed border-ink-200/50 shrink-0" aria-hidden />
            <span><span className="font-medium">optional</span> — depth detour</span>
          </li>
        </ul>
        <p className="text-[11px] text-ink-100/65 leading-snug pt-1">
          Read top to bottom for the linear path; click any node for resources.
        </p>
      </div>
      <div className="px-4 py-3 border-b border-ink-900/60">
        <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-100/55">
          The path
        </div>
      </div>
      <nav className="px-2 py-2 space-y-0.5">
        {stages.map((s) => {
          const color = palette[s.id];
          const active = focusedStageId === s.id;
          return (
            <button
              key={s.id}
              onClick={() => onFocus(s.id)}
              className={`w-full text-left px-2 py-1.5 rounded-sm flex items-baseline gap-2 transition-colors ${
                active ? "bg-ink-900/80" : "hover:bg-ink-900/50"
              }`}
              title={active ? "Click again to clear focus" : "Click to focus this stage"}
            >
              <span
                className="inline-block w-2 h-2 rounded-sm shrink-0 translate-y-[1px]"
                style={{ background: color }}
                aria-hidden
              />
              <span className="font-mono text-[10px] text-ink-100/55 shrink-0">
                {String(s.stageNumber).padStart(2, "0")}
              </span>
              <span className="font-serif text-sm text-ink-50/90 leading-snug">{s.title}</span>
            </button>
          );
        })}
      </nav>
      <div className="mt-auto px-4 py-3 border-t border-ink-900/60 text-[10px] uppercase tracking-wider text-ink-100/50">
        <kbd className="font-mono px-1 border border-ink-900 rounded-sm">/</kbd> search ·{" "}
        <kbd className="font-mono px-1 border border-ink-900 rounded-sm">esc</kbd> close ·{" "}
        <kbd className="font-mono px-1 border border-ink-900 rounded-sm">t</kbd> theme
      </div>
    </aside>
  );
}
