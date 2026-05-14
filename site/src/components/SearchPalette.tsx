import { useEffect, useMemo, useRef, useState } from "react";
import type { Stage } from "../types";

interface Props {
  stages: Stage[];
  onClose: () => void;
  onSelect: (id: string) => void;
}

interface Hit {
  id: string;
  label: string;
  stageTitle: string;
  stageNumber: number;
  desc: string;
}

export function SearchPalette({ stages, onClose, onSelect }: Props) {
  const [q, setQ] = useState("");
  const [active, setActive] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const all: Hit[] = useMemo(
    () =>
      stages.flatMap((s) =>
        s.nodes.map((n) => ({
          id: n.id,
          label: n.label,
          stageTitle: s.title,
          stageNumber: s.stageNumber,
          desc: n.description,
        })),
      ),
    [stages],
  );

  const hits = useMemo(() => {
    const query = q.trim().toLowerCase();
    if (!query) return all.slice(0, 24);
    return all
      .map((h) => {
        const inLabel = h.label.toLowerCase().includes(query);
        const inDesc = h.desc.toLowerCase().includes(query);
        const inStage = h.stageTitle.toLowerCase().includes(query);
        let score = 0;
        if (inLabel) score += 8;
        if (inDesc) score += 2;
        if (inStage) score += 1;
        return { h, score };
      })
      .filter((x) => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 24)
      .map((x) => x.h);
  }, [q, all]);

  useEffect(() => {
    if (active >= hits.length) setActive(Math.max(0, hits.length - 1));
  }, [hits.length, active]);

  const onKey = (e: React.KeyboardEvent) => {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActive((a) => Math.min(a + 1, hits.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive((a) => Math.max(a - 1, 0));
    } else if (e.key === "Enter") {
      e.preventDefault();
      const hit = hits[active];
      if (hit) onSelect(hit.id);
    }
  };

  return (
    <div
      className="fixed inset-0 z-30 bg-black/60 backdrop-blur-sm flex items-start justify-center p-4 sm:p-12"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-label="Search nodes"
    >
      <div
        className="w-full max-w-xl bg-ink-950 border border-ink-900 rounded-md shadow-xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        <input
          ref={inputRef}
          value={q}
          onChange={(e) => {
            setQ(e.target.value);
            setActive(0);
          }}
          onKeyDown={onKey}
          placeholder="Search nodes by label or description…"
          className="w-full bg-transparent text-ink-50 placeholder:text-ink-100/40 px-4 py-3 outline-none border-b border-ink-900 font-sans text-sm"
        />
        <ul className="max-h-[60vh] overflow-y-auto">
          {hits.length === 0 ? (
            <li className="px-4 py-6 text-sm text-ink-100/55 italic text-center">
              No matching nodes.
            </li>
          ) : (
            hits.map((h, i) => (
              <li key={h.id}>
                <button
                  onMouseEnter={() => setActive(i)}
                  onClick={() => onSelect(h.id)}
                  className={`w-full text-left px-4 py-2.5 flex items-baseline gap-3 ${
                    i === active ? "bg-ink-900/80" : "hover:bg-ink-900/50"
                  }`}
                >
                  <span className="font-mono text-[10px] text-ink-100/55 shrink-0">
                    {String(h.stageNumber).padStart(2, "0")}
                  </span>
                  <span className="font-serif text-sm text-ink-50/95 truncate">{h.label}</span>
                  <span className="ml-auto text-[10px] uppercase tracking-wider text-ink-100/50 shrink-0">
                    {h.stageTitle}
                  </span>
                </button>
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}
