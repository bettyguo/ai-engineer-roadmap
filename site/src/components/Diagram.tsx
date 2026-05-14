import { useMemo } from "react";
import {
  ReactFlow,
  ReactFlowProvider,
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
  type Node,
  type Edge,
  type NodeTypes,
} from "@xyflow/react";
import type { CrossStageEdge, Stage } from "../types";
import { NodeCard } from "./NodeCard";
import { StageHeader } from "./StageHeader";

interface Props {
  stages: Stage[];
  palette: Record<string, string>;
  crossStageEdges: CrossStageEdge[];
  focusedStageId: string | null;
  selectedId: string | null;
  onSelect: (id: string | null) => void;
}

// Layout: stages stack vertically. Each stage gets a horizontal band.
// Within a stage, nodes use their hand-laid {x, y} from the data, shifted
// down by the stage's band offset.

const STAGE_BAND_HEIGHT = 720; // generous; gives each stage breathing room
const STAGE_LABEL_OFFSET_Y = -120;
const NODE_X_OFFSET = 80;

const nodeTypes: NodeTypes = {
  card: NodeCard as unknown as NodeTypes[string],
  stageHeader: StageHeader as unknown as NodeTypes[string],
};

export function Diagram({
  stages,
  palette,
  crossStageEdges,
  focusedStageId,
  selectedId,
  onSelect,
}: Props) {
  const { nodes, edges } = useMemo(() => {
    const rfNodes: Node[] = [];
    const rfEdges: Edge[] = [];

    stages.forEach((stage, stageIdx) => {
      const yOffset = stageIdx * STAGE_BAND_HEIGHT;
      const stageColor = palette[stage.id] || "#888888";
      const dimmed = focusedStageId !== null && focusedStageId !== stage.id;

      rfNodes.push({
        id: `stage-${stage.id}`,
        type: "stageHeader",
        position: { x: 0, y: yOffset + STAGE_LABEL_OFFSET_Y },
        data: {
          title: stage.title,
          number: stage.stageNumber,
          blurb: stage.blurb,
          color: stageColor,
          dimmed,
        },
        draggable: false,
        selectable: false,
      });

      stage.nodes.forEach((n) => {
        rfNodes.push({
          id: n.id,
          type: "card",
          position: {
            x: n.position.x + NODE_X_OFFSET,
            y: n.position.y + yOffset,
          },
          data: {
            label: n.label,
            status: n.status,
            color: stageColor,
            dimmed,
            selected: selectedId === n.id,
            resourceCount: n.resources.length,
          },
          draggable: false,
        });

        n.dependsOn.forEach((depId) => {
          rfEdges.push({
            id: `${depId}->${n.id}`,
            source: depId,
            target: n.id,
            type: "smoothstep",
            style: { strokeOpacity: dimmed ? 0.18 : 0.55 },
          });
        });

        n.crossStageDependsOn.forEach((depId) => {
          rfEdges.push({
            id: `${depId}->${n.id}@cross`,
            source: depId,
            target: n.id,
            type: "smoothstep",
            className: "react-flow__edge--dotted",
            style: { strokeOpacity: 0.4 },
          });
        });
      });

      if (stageIdx > 0) {
        const prevStage = stages[stageIdx - 1];
        rfEdges.push({
          id: `stage-${prevStage.id}->stage-${stage.id}`,
          source: `stage-${prevStage.id}`,
          target: `stage-${stage.id}`,
          type: "straight",
          style: { strokeOpacity: 0.15, strokeWidth: 2 },
        });
      }
    });

    crossStageEdges.forEach((edge, i) => {
      rfEdges.push({
        id: `xstage-${i}-${edge.from}->${edge.to}`,
        source: edge.from,
        target: edge.to,
        type: "smoothstep",
        className: "react-flow__edge--dotted",
        style: { strokeOpacity: 0.32 },
      });
    });

    return { nodes: rfNodes, edges: rfEdges };
  }, [stages, palette, crossStageEdges, focusedStageId, selectedId]);

  return (
    <ReactFlowProvider>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        fitView
        fitViewOptions={{ padding: 0.18, minZoom: 0.25, maxZoom: 1.2 }}
        minZoom={0.15}
        maxZoom={1.6}
        onNodeClick={(_e, n) => {
          if (n.type === "card") onSelect(n.id);
        }}
        onPaneClick={() => onSelect(null)}
        nodesDraggable={false}
        proOptions={{ hideAttribution: true }}
      >
        <Background variant={BackgroundVariant.Dots} gap={28} size={1} />
        <Controls showInteractive={false} />
        <MiniMap
          pannable
          zoomable
          nodeColor={(node) => {
            if (node.type === "stageHeader") return "transparent";
            const c = (node.data as { color?: string } | undefined)?.color;
            return c || "#999";
          }}
          maskColor="rgba(5, 5, 5, 0.7)"
        />
      </ReactFlow>
    </ReactFlowProvider>
  );
}
