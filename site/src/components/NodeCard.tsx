import { Handle, Position } from "@xyflow/react";
import type { NodeProps } from "@xyflow/react";

interface CardData {
  label: string;
  status: "core" | "recommended" | "optional";
  color: string;
  dimmed: boolean;
  selected: boolean;
  resourceCount: number;
}

/* Visual grammar:
   - core         = solid filled background tinted with the stage color
   - recommended  = outlined card with a thin tinted accent
   - optional     = hatched / muted card
   - selected     = ring + slight scale
   - dimmed       = reduced opacity when another stage is focused
*/

export function NodeCard({ data }: NodeProps) {
  const { label, status, color, dimmed, selected, resourceCount } = data as unknown as CardData;

  const base =
    "rf-node relative rounded-md px-3 py-2.5 cursor-pointer select-none transition-all duration-150";

  const sizing = "min-w-[180px] max-w-[240px]";

  let appearance = "";
  if (status === "core") {
    appearance =
      "text-ink-50 font-medium shadow-sm";
  } else if (status === "recommended") {
    appearance =
      "text-ink-50 font-medium border";
  } else {
    appearance =
      "text-ink-100 font-normal border border-dashed opacity-90";
  }

  const ring = selected ? "ring-2 ring-offset-2 ring-offset-ink-950" : "";
  const dim = dimmed ? "opacity-25" : "";

  const fillColor = status === "core" ? hexWithAlpha(color, 0.92) : "transparent";
  const borderColor =
    status === "recommended" ? hexWithAlpha(color, 0.85) : hexWithAlpha(color, 0.45);

  return (
    <div
      className={`${base} ${sizing} ${appearance} ${ring} ${dim}`}
      style={{
        background: fillColor,
        borderColor,
        ...(selected ? { boxShadow: `0 0 0 2px ${color}` } : {}),
      }}
    >
      <Handle type="target" position={Position.Left} className="!opacity-0" />
      <div className="text-[13px] leading-snug font-serif">{label}</div>
      <div className="mt-1 flex items-center gap-2 text-[10px] uppercase tracking-wider opacity-80">
        <span>{status}</span>
        {resourceCount > 0 && (
          <span className="rounded-sm bg-black/30 px-1.5 py-0.5">
            {resourceCount} {resourceCount === 1 ? "resource" : "resources"}
          </span>
        )}
      </div>
      <Handle type="source" position={Position.Right} className="!opacity-0" />
    </div>
  );
}

function hexWithAlpha(hex: string, alpha: number): string {
  const m = /^#?([0-9a-f]{6})$/i.exec(hex);
  if (!m) return hex;
  const r = parseInt(m[1].slice(0, 2), 16);
  const g = parseInt(m[1].slice(2, 4), 16);
  const b = parseInt(m[1].slice(4, 6), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}
