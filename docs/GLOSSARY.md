# Glossary

Terms that appear across the roadmap, with the canonical node where
each is defined. Use this as a forward index when a stage-5 node
references something defined in stage-3.

Each entry: term, one-sentence working definition, the node where
it's developed.

---

## A

**Adam / AdamW** — Adaptive-learning-rate optimizer; the default for
most deep-learning training in 2026. See [`dl-optimizers`](../roadmap-data/stages/04-dl-fundamentals.json).

**Agent** — An LLM-driven program that observes, plans, and acts via
tools in a loop, with some notion of memory. See [`agent-tool-use`](../roadmap-data/stages/09-agents-harnesses.json).

**Alignment** — The practice of training a model to behave helpfully,
harmlessly, and honestly. See [`frontier-alignment-basics`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**ANN (Approximate Nearest Neighbor)** — Fast vector-similarity search
that trades exact recall for speed; HNSW and IVF are the dominant
indexes. See [`rag-vector-stores`](../roadmap-data/stages/08-retrieval-rag.json).

**Attention** — A mechanism that lets every token in a sequence
selectively read from every other token. The core operation of the
transformer. See [`tx-self-attention`](../roadmap-data/stages/05-transformers-llm-internals.json).

**AWQ** — Activation-aware Weight Quantization; a 4-bit weight-only
quantization scheme. See [`inf-quantization`](../roadmap-data/stages/07-inference-serving.json).

## B

**Backpropagation** — The chain rule applied at scale to compute
gradients of a loss with respect to model weights. See [`dl-backprop`](../roadmap-data/stages/04-dl-fundamentals.json).

**Batch / batching** — Running multiple inputs through a model
together for throughput. *Continuous batching* in LLM serving allows
new requests to join an in-flight batch. See [`inf-batching`](../roadmap-data/stages/07-inference-serving.json).

**Bias-variance tradeoff** — The frame for why a model underfits or
overfits; regularization is the dial. See [`ml-bias-variance-regularization`](../roadmap-data/stages/03-ml-fundamentals.json).

**BPE (Byte-Pair Encoding)** — A subword tokenization scheme; the
mechanism behind almost every modern tokenizer. See [`tx-tokenization`](../roadmap-data/stages/05-transformers-llm-internals.json).

**BF16 / FP16 / FP8** — Reduced-precision floating-point formats used
for training and inference. See [`math-numerical-floating-point`](../roadmap-data/stages/01-prerequisites-math.json).

## C

**Chain-of-thought (CoT)** — Prompting a model to reason step-by-step;
also a training target for reasoning models. See [`agent-planning-patterns`](../roadmap-data/stages/09-agents-harnesses.json)
and [`frontier-reasoning-models`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**Chunking** — Splitting a document into pieces that fit a retrieval
unit and an embedding context. See [`rag-chunking`](../roadmap-data/stages/08-retrieval-rag.json).

**CLIP** — The contrastive image-text model that underpins most
vision-language stacks. See [`frontier-multimodal`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**Computer-use agent** — An agent that interacts with a real computer
via screen, mouse, and keyboard, with no purpose-built APIs. See
[`agent-computer-use`](../roadmap-data/stages/09-agents-harnesses.json).

**Constitutional AI (CAI)** — Anthropic's method for training
harmlessness from AI feedback rather than human labels. See the
resource on [`frontier-alignment-basics`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**Continuous batching** — Serving-time batching that admits new
requests into a running batch. See [`inf-batching`](../roadmap-data/stages/07-inference-serving.json).

**Cross-encoder** — A reranker that scores a (query, document) pair
jointly, instead of scoring them via separate embeddings. See
[`rag-reranking`](../roadmap-data/stages/08-retrieval-rag.json).

## D

**Disaggregated inference** — Serving architecture that runs prefill
and decode on separate GPU pools. See [`inf-disaggregated`](../roadmap-data/stages/07-inference-serving.json).

**DPO (Direct Preference Optimization)** — A reward-model-free
preference-learning method; the practical default in 2026. See
[`train-dpo-preference`](../roadmap-data/stages/06-training-finetuning.json).

**Distillation** — Training a small student model to mimic a large
teacher's outputs. See [`train-distillation-compression`](../roadmap-data/stages/06-training-finetuning.json).

## E

**Embedding** — A vector representation of an input (token, sentence,
image) in a learned space. See [`dl-embeddings-representations`](../roadmap-data/stages/04-dl-fundamentals.json)
for the concept and [`rag-embeddings`](../roadmap-data/stages/08-retrieval-rag.json)
for retrieval-time use.

**Evaluation harness** — A framework for running standardized
benchmarks reproducibly. `lm-evaluation-harness`, HELM, Inspect. See
[`eval-harnesses`](../roadmap-data/stages/10-evaluation-observability.json).

## F

**FlashAttention** — A fused, memory-aware attention kernel that's
both faster and lower-VRAM than the naive implementation. See [`inf-loop-kv-cache`](../roadmap-data/stages/07-inference-serving.json).

**FSDP (Fully Sharded Data Parallel)** — PyTorch's sharded data-
parallel training scheme; the dominant scheme for ≥7B-param training.
See [`train-distributed-infra`](../roadmap-data/stages/06-training-finetuning.json).

**Fine-tuning** — Training a pre-trained model on a smaller, task-
specific dataset. Encompasses SFT, instruction tuning, DPO, LoRA.
See Stage 6.

**Function calling** — A model API that lets the model emit
structured calls to declared tools. See [`agent-function-calling-mcp`](../roadmap-data/stages/09-agents-harnesses.json).

## G

**GGUF** — A file format for quantized LLM weights used by
`llama.cpp` and its ecosystem. See [`inf-quantization`](../roadmap-data/stages/07-inference-serving.json).

**Golden dataset** — A small, hand-curated eval set with rubric scoring;
the regression suite of LLM development. See [`eval-golden-datasets`](../roadmap-data/stages/10-evaluation-observability.json).

**GQA (Grouped-Query Attention)** — An attention variant that
shares K/V across query groups to shrink KV-cache size. See [`tx-model-anatomy`](../roadmap-data/stages/05-transformers-llm-internals.json).

**GraphRAG** — A retrieval pattern that uses a knowledge graph as the
retrieval substrate. See [`rag-advanced-contextual-graph`](../roadmap-data/stages/08-retrieval-rag.json).

## H

**Hybrid search** — Combining sparse (BM25) and dense (vector)
retrieval, typically with reciprocal rank fusion. See [`rag-hybrid-search`](../roadmap-data/stages/08-retrieval-rag.json).

**HNSW** — Hierarchical Navigable Small World; an ANN index. See
[`rag-vector-stores`](../roadmap-data/stages/08-retrieval-rag.json).

## I

**Instruction tuning** — SFT with instruction-following data so the
base model becomes a usable assistant. See [`train-instruction-tuning`](../roadmap-data/stages/06-training-finetuning.json).

## J

**Jailbreak** — A prompt that bypasses a model's safety training. See
[`frontier-jailbreaks-prompt-injection`](../roadmap-data/stages/12-safety-alignment-frontier.json).

## K

**KV cache** — The cached attention keys and values from prior tokens;
the data structure that makes autoregressive generation linear, not
quadratic. See [`inf-loop-kv-cache`](../roadmap-data/stages/07-inference-serving.json).

## L

**LLM (Large Language Model)** — A transformer-based decoder-only model
trained on next-token prediction at scale. See [`tx-model-anatomy`](../roadmap-data/stages/05-transformers-llm-internals.json).

**LLM-as-judge** — Using a model to grade another model's outputs.
See [`eval-llm-as-judge`](../roadmap-data/stages/10-evaluation-observability.json).

**LLaVA** — The reference open vision-language model: frozen CLIP
encoder + projector + LLM, trained on visual instruction-following
data. See [`frontier-multimodal`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**LoRA / QLoRA** — Parameter-efficient fine-tuning via low-rank
decomposition (QLoRA adds quantization). See [`train-lora-qlora-adapters`](../roadmap-data/stages/06-training-finetuning.json).

## M

**Mamba** — A selective state-space-model architecture; the
post-transformer alternative being seriously explored in 2026. See
[`frontier-state-space-models`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**Mechanistic interpretability ("mech-interp")** — Reverse-engineering
the algorithms inside a trained model. See [`frontier-mech-interp`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**MCP (Model Context Protocol)** — A cross-provider standard for
exposing tools to LLMs. See [`agent-function-calling-mcp`](../roadmap-data/stages/09-agents-harnesses.json).

**MoE (Mixture of Experts)** — A model architecture that routes each
token to a subset of expert sub-networks for capacity-with-efficiency.
See [`tx-model-anatomy`](../roadmap-data/stages/05-transformers-llm-internals.json).

## N

**Normalization** — Layer norm, RMS norm, batch norm; what stabilizes
deep-network training. See [`dl-init-normalization`](../roadmap-data/stages/04-dl-fundamentals.json).

## P

**Prefill / decode** — The two phases of LLM inference: prefill is
the parallel pass over the prompt; decode is the autoregressive
per-token loop. See [`inf-loop-kv-cache`](../roadmap-data/stages/07-inference-serving.json).

**Prompt injection** — An attack that hides instructions inside
content the model will process. See [`frontier-jailbreaks-prompt-injection`](../roadmap-data/stages/12-safety-alignment-frontier.json).

## Q

**Quantization** — Reducing model-weight precision (INT8, INT4) for
smaller memory and faster inference, at some quality cost. See
[`inf-quantization`](../roadmap-data/stages/07-inference-serving.json).

## R

**RAG (Retrieval-Augmented Generation)** — Letting an LLM read
retrieved context at inference time, rather than relying only on its
pretraining. See Stage 8.

**ReAct** — A planning pattern (Reasoning + Action) where the model
alternates thought and tool-call steps. See [`agent-planning-patterns`](../roadmap-data/stages/09-agents-harnesses.json).

**Reranking** — A second-stage retrieval step that scores
(query, candidate) pairs more carefully. See [`rag-reranking`](../roadmap-data/stages/08-retrieval-rag.json).

**RLHF (Reinforcement Learning from Human Feedback)** — Reward-model
+ PPO post-training; the InstructGPT recipe. See [`train-rlhf`](../roadmap-data/stages/06-training-finetuning.json).

**RoPE (Rotary Position Embedding)** — The dominant positional
encoding in 2026. See [`tx-positional-encoding-rope`](../roadmap-data/stages/05-transformers-llm-internals.json).

## S

**SAE (Sparse Autoencoder)** — A mech-interp tool for finding
interpretable features in a model's residual stream. See [`frontier-mech-interp`](../roadmap-data/stages/12-safety-alignment-frontier.json).

**Scaling laws** — Empirical curves relating model size, data size,
compute, and loss. See [`tx-scaling-laws`](../roadmap-data/stages/05-transformers-llm-internals.json).

**SGLang** — A modern LLM serving engine. See [`inf-engines-vllm-tgi-sglang`](../roadmap-data/stages/07-inference-serving.json).

**SFT (Supervised Fine-Tuning)** — Standard fine-tuning on labeled
prompt-response pairs. See [`train-sft`](../roadmap-data/stages/06-training-finetuning.json).

**Speculative decoding** — Letting a small draft model propose tokens
that a big target model verifies; preserves output distribution while
running faster. See [`inf-speculative-decoding`](../roadmap-data/stages/07-inference-serving.json).

**SLO (Service-Level Objective)** — A measurable target for a service's
quality (e.g., p95 latency < 800ms). See [`prod-latency-slos`](../roadmap-data/stages/11-deployment-production.json).

**Structured output** — Forcing a model to emit valid JSON, a schema,
or grammar-constrained text. See [`inf-structured-output`](../roadmap-data/stages/07-inference-serving.json).

**SSM (State Space Model)** — A linear-time sequence model; the
non-attention alternative explored by Mamba. See [`frontier-state-space-models`](../roadmap-data/stages/12-safety-alignment-frontier.json).

## T

**Tokenization** — Splitting text into tokens; the LLM's input unit.
See [`tx-tokenization`](../roadmap-data/stages/05-transformers-llm-internals.json).

**Tracing (LLM observability)** — Per-request logs of prompts,
responses, tool calls, costs, and latencies. See [`eval-tracing-observability`](../roadmap-data/stages/10-evaluation-observability.json).

**Transformer** — The decoder-only-block architecture that won. See
[`tx-architecture`](../roadmap-data/stages/05-transformers-llm-internals.json).

**TTFT / TPOT** — Time-To-First-Token / Time-Per-Output-Token; the
two latency metrics that matter in LLM serving. See [`inf-latency-throughput`](../roadmap-data/stages/07-inference-serving.json).

## V

**vLLM** — The widely-used open-source LLM serving engine. See
[`inf-engines-vllm-tgi-sglang`](../roadmap-data/stages/07-inference-serving.json).

**Vector store** — A database optimized for ANN search over
embeddings. See [`rag-vector-stores`](../roadmap-data/stages/08-retrieval-rag.json).

## Y / Z

(Reserved for terms that haven't graduated to first-class nodes.
Submit a [`Suggest a resource`](../.github/ISSUE_TEMPLATE/add-resource.yml)
or [`Propose a new node`](../.github/ISSUE_TEMPLATE/add-node.yml) issue
to expand the glossary.)
