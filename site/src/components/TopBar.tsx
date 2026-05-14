import type { Manifest } from "../types";

interface Props {
  manifest: Manifest;
  onSearchClick: () => void;
  theme: "dark" | "light";
  onToggleTheme: () => void;
}

export function TopBar({ manifest, onSearchClick, theme, onToggleTheme }: Props) {
  return (
    <header className="border-b border-ink-900/60 bg-ink-950/95 backdrop-blur sticky top-0 z-20">
      <div className="flex items-center justify-between px-5 py-3 gap-4">
        <div className="flex items-baseline gap-3 min-w-0">
          <a href="#" className="font-serif text-base font-semibold tracking-tight">
            <span className="signature-underline">AI Engineer Roadmap</span>
          </a>
          <span className="hidden md:inline text-xs text-ink-100/55 truncate">
            curated by {manifest.curator.name.split("(")[0].trim()} · {manifest.curator.affiliation.split(",")[0]}
          </span>
        </div>
        <div className="flex items-center gap-2">
          <span className="hidden sm:inline text-[10px] uppercase tracking-wider text-ink-100/60">
            updated {manifest.lastUpdated}
          </span>
          <button
            onClick={onSearchClick}
            className="text-xs font-mono px-2 py-1 border border-ink-900 rounded-sm hover:border-ink-200/40 hover:text-ink-50"
            aria-label="Open search"
            title="Search (/)"
          >
            / search
          </button>
          <button
            onClick={onToggleTheme}
            className="text-xs font-mono px-2 py-1 border border-ink-900 rounded-sm hover:border-ink-200/40 hover:text-ink-50"
            aria-label="Toggle theme"
            title="Toggle theme (t)"
          >
            {theme === "dark" ? "paper" : "ink"}
          </button>
          <a
            href={manifest.repo}
            target="_blank"
            rel="noopener noreferrer"
            className="text-xs font-mono px-2 py-1 border border-ink-900 rounded-sm hover:border-ink-200/40 hover:text-ink-50"
          >
            github
          </a>
        </div>
      </div>
    </header>
  );
}
