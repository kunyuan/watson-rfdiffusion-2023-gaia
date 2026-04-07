# watson-rfdiffusion-2023-gaia

Gaia knowledge package: Watson et al. 2023 — De novo design of protein structure and function with RFdiffusion (Nature)

[![Interactive Paper](https://img.shields.io/badge/📖_Interactive_Paper-GitHub_Pages-blue)](https://kunyuan.github.io/watson-rfdiffusion-2023-gaia/) [![Knowledge Reference](https://img.shields.io/badge/📚_Reference-Wiki-green)](https://github.com/kunyuan/watson-rfdiffusion-2023-gaia/wiki)

## Overview

```mermaid
graph TD
    rfdiffusion_broad_success["RFdiffusion achieves broad design success ★ (0.50 → 0.76)"]:::exported
    pipeline_description["RFdiffusion design pipeline (0.50 → 1.00)"]:::derived
    symmetric_high_success["High in silico success for symmetric oligomers ★ (0.50 → 1.00)"]:::exported
    rfdiffusion_benchmark_performance["RFdiffusion solves 23/25 benchmark problems ★ (0.50 → 1.00)"]:::exported
    binder_success_rate["19% binder success rate — 100× improvement over Rosetta ★ (0.50 → 1.00)"]:::exported
    ha20_atomic_accuracy["RFdiffusion achieves atomic-level accuracy in binder design ★ (0.50 → 0.87)"]:::exported
    comprehensive_improvement["RFdiffusion is comprehensive improvement over prior methods ★ (0.50 → 0.99)"]:::exported
    generality_claim["RFdiffusion enables protein design from minimal specifications ★ (0.50 → 0.61)"]:::exported
    strat_7(["noisy_and"]):::weak
    pipeline_description --> strat_7
    strat_7 --> symmetric_high_success
    strat_14(["noisy_and"]):::weak
    pipeline_description --> strat_14
    strat_14 --> rfdiffusion_benchmark_performance
    strat_27(["noisy_and"]):::weak
    pipeline_description --> strat_27
    strat_27 --> binder_success_rate
    strat_32(["noisy_and"]):::weak
    binder_success_rate --> strat_32
    strat_32 --> ha20_atomic_accuracy
    strat_34(["abduction"]):::weak
    rfdiffusion_benchmark_performance --> strat_34
    strat_34 --> comprehensive_improvement
    strat_35(["abduction"]):::weak
    binder_success_rate --> strat_35
    strat_35 --> comprehensive_improvement
    strat_36(["induction"]):::weak
    rfdiffusion_benchmark_performance --> strat_36
    binder_success_rate --> strat_36
    strat_36 --> comprehensive_improvement
    strat_40(["noisy_and"]):::weak
    comprehensive_improvement --> strat_40
    ha20_atomic_accuracy --> strat_40
    strat_40 --> rfdiffusion_broad_success
    strat_41(["noisy_and"]):::weak
    rfdiffusion_broad_success --> strat_41
    strat_41 --> generality_claim

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Belief |
|-------|---------|--------|
| binder_success_rate | The overall experimental success rate for RFdiffusion binders (binding at or ... | 1.00 |
| comprehensive_improvement | RFdiffusion is a comprehensive improvement over current protein design method... | 0.99 |
| generality_claim | In a manner analogous to networks that produce images from user-specified inp... | 0.61 |
| ha20_atomic_accuracy | The near-perfect agreement between the cryo-EM structure and the RFdiffusion ... | 0.87 |
| rfdiffusion_benchmark_performance | RFdiffusion solves 23 of the 25 benchmark motif-scaffolding problems, compare... | 1.00 |
| rfdiffusion_broad_success | RFdiffusion achieves outstanding performance on unconditional and topology-co... | 0.76 |
| symmetric_high_success | Despite not being trained on symmetric inputs, RFdiffusion generates symmetri... | 1.00 |

<!-- content:start -->
<!-- content:end -->
