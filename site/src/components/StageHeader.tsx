import { Handle, Position } from "@xyflow/react";
import type { NodeProps } from "@xyflow/react";

interface StageHeaderData {
  title: string;
  number: number;
  blurb: string;
  color: string;
  dimmed: boolean;
}

export function StageHeader({ data }: NodeProps) {
  const { title, number, blurb, color, dimmed } = data as unknown as StageHeaderData;
  return (
    <div
      className={`relative max-w-[640px] ${dimmed ? "opacity-25" : ""}`}
      style={{ pointerEvents: "none" }}
    >
      <Handle type="target" position={Position.Top} className="!opacity-0" />
      <div className="flex items-baseline gap-3">
        <div
          className="font-mono text-xs uppercase tracking-[0.18em]"
          style={{ color }}
        >
          Stage {String(number).padStart(2, "0")}
        </div>
      </div>
      <div className="font-serif text-2xl font-semibold mt-1">
        <span className="signature-underline" style={{ color }}>
          {title}
        </span>
      </div>
      <div className="mt-2 text-sm text-ink-100/80 max-w-[560px] leading-relaxed">
        {blurb}
      </div>
      <Handle type="source" position={Position.Bottom} className="!opacity-0" />
    </div>
  );
}
