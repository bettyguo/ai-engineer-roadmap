// Shared TS types for the renderer. Mirrors roadmap-data/schema/*.json.
// The Python build step (tools/build.py) emits data.generated.ts that
// imports this type, so any schema change must update this file too.

export type NodeStatus = "core" | "recommended" | "optional";

export type ResourceType =
  | "paper"
  | "course"
  | "repo"
  | "book"
  | "video"
  | "blog"
  | "tool"
  | "official"
  | "interactive";

export type Difficulty = "intro" | "intermediate" | "advanced";

export interface Resource {
  title: string;
  author?: string;
  year?: number;
  type: ResourceType;
  url: string;
  annotation: string;
  difficulty: Difficulty;
  free: boolean;
  addedAt: string;
  verifiedAt: string;
  verifiedBy?: string;
}

export interface Position {
  x: number;
  y: number;
}

export interface RoadmapNode {
  id: string;
  label: string;
  status: NodeStatus;
  description: string;
  doneWhen: string;
  position: Position;
  dependsOn: string[];
  crossStageDependsOn: string[];
  resources: Resource[];
}

export interface SidewaysLink {
  to: string;
  url: string;
  label: string;
  blurb: string;
}

export interface Stage {
  id: string;
  stageNumber: number;
  title: string;
  blurb: string;
  color: string;
  nodes: RoadmapNode[];
  sidewaysLinks?: SidewaysLink[];
}

export interface CrossStageEdge {
  from: string;
  to: string;
  kind: string;
}

export interface Peer {
  id: string;
  title: string;
  role: string;
  blurb: string;
  url: string;
  openWhen: string;
}

export interface Curator {
  name: string;
  affiliation: string;
  advisor?: string;
  github: string;
  orcid: string;
}

export interface Manifest {
  schemaVersion: string;
  title: string;
  tagline: string;
  curator: Curator;
  license: { content: string; code: string };
  lastUpdated: string;
  liveSite: string;
  repo: string;
  stages: string[];
  palette: Record<string, string>;
}

export interface RoadmapData {
  manifest: Manifest;
  stages: Stage[];
  peers: Peer[];
  crossStageEdges: CrossStageEdge[];
}
