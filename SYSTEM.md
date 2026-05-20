# 技术架构

## 系统组成

- 飞书群聊: AI会议室中转器 (WebSocket)
- Hermes Agent: Windows服务，运行evolver.py
- GitHub: ai-groupchat-evolution 仓库

## 演进循环

1. Cronjob每2小时触发evolover.py
2. 连接GitHub，扫描顶级AI开源仓库
3. KNOWN_PATTERNS精准识别代码基因
4. 基因存入gene_bank.json（去重）
5. 报告推送飞书群聊
6. gene_bank.json + evolution_log.json 推送GitHub

## 基因来源

| 仓库 | 专注 |
|------|------|
| vllm/vllm | PagedAttention、ContinuousBatching |
| ggml-org/llama.cpp | K-Quantization |
| flashinfer-team/flashinfer | FlashAttention |
