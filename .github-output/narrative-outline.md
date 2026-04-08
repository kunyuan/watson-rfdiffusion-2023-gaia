# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Noise-free reverse trajectories often improve success

1. **Alternative: disordered aggregates mimicking icosahedral symmetry** (prior: 0.08 → belief: 0.08)
   - → supports: symmetric_high_success

2. **Alternative: structural mimicry in nsEM** (prior: 0.12 → belief: 0.12)
   - → supports: symmetric_high_success

3. **Alternative: training set memorization** (prior: 0.15 → belief: 0.15)
   - → supports: rfdiffusion_benchmark_performance

4. **Alternative: recapitulating PDB binding modes** (prior: 0.15 → belief: 0.15)
   - → supports: binder_success_rate

5. **Alternative: non-specific binding in p53-MDM2 screens** (prior: 0.18 → belief: 0.18)
   - → supports: rfdiffusion_benchmark_performance

6. **Alternative: non-specific adhesion** (prior: 0.18 → belief: 0.18)
   - → supports: binder_success_rate

7. **Alternative: noise-free improvement is overfitting** (prior: 0.20 → belief: 0.20)
   - → supports: rfdiffusion_benchmark_performance

8. **Alternative: coincidental SEC profiles** (prior: 0.30 → belief: 0.30)
   - → supports: symmetric_high_success

9. **Limitations of prior protein diffusion methods** (prior: 0.85 → belief: 1.00)
   - → supports: symmetric_high_success, binder_success_rate, rfdiffusion_benchmark_performance

10. **RFjoint Inpainting limitations** (prior: 0.85 → belief: 1.00)
   - → supports: symmetric_high_success, binder_success_rate, rfdiffusion_benchmark_performance

11. **Pretraining from RF weights is critical** (prior: 0.88 → belief: 1.00)
   - → supports: symmetric_high_success, binder_success_rate, rfdiffusion_benchmark_performance

12. **Self-conditioning improves RFdiffusion performance** (prior: 0.88 → belief: 1.00)
   - → supports: symmetric_high_success, binder_success_rate, rfdiffusion_benchmark_performance

13. **DDPM properties suited for protein design** (prior: 0.90 → belief: 1.00)
   - → supports: symmetric_high_success, binder_success_rate, rfdiffusion_benchmark_performance

14. **Success rate improvement attributed to RFdiffusion + AF2 filtering** (prior: 0.75 → belief: 1.00)
   - → supports: binder_success_rate

15. **Iterative denoising generation process** (prior: 0.92 → belief: 1.00)
   - → supports: symmetric_high_success, binder_success_rate, rfdiffusion_benchmark_performance

16. **Prior binder design methods had low success rates** (prior: 0.88 → belief: 1.00)
   - → supports: binder_success_rate

17. **RFjoint Inpainting solves 19/25 benchmark problems** (prior: 0.88 → belief: 1.00)
   - → supports: rfdiffusion_benchmark_performance

18. **Hallucination solves 15/25 benchmark problems** (prior: 0.88 → belief: 1.00)
   - → supports: rfdiffusion_benchmark_performance

19. **Novel binding interfaces distinct from PDB** (prior: 0.88 → belief: 1.00)
   - → supports: binder_success_rate

20. **IL-7Rα binders show site-specific binding** (prior: 0.88 → belief: 1.00)
   - → supports: binder_success_rate

21. **Icosahedral assembly HE0902 validated by nsEM** (prior: 0.88 → belief: 1.00)
   - → supports: symmetric_high_success

22. **p53-MDM2 binder scaffolding: 55/96 designs show binding** (prior: 0.92 → belief: 1.00)
   - → supports: rfdiffusion_benchmark_performance

23. **nsEM confirms cyclic oligomer structures** (prior: 0.92 → belief: 1.00)
   - → supports: symmetric_high_success

24. **SEC validates oligomeric states** (prior: 0.92 → belief: 1.00)
   - → supports: symmetric_high_success

25. **Scaffolding success independent of training set membership** (prior: 0.88 → belief: 1.00)
   - → supports: rfdiffusion_benchmark_performance

26. **Noise-free reverse trajectories often improve success** (prior: 0.88 → belief: 1.00)
   - → supports: rfdiffusion_benchmark_performance

## Cryo-EM structure of HA_20-HA complex at 2.9 Å

27. **Alternative: HA_20 adopts alternative conformation** (prior: 0.05 → belief: 0.10)
   - → supports: ha20_atomic_accuracy

28. **Cryo-EM structure of HA_20-HA complex at 2.9 Å** (prior: 0.95 → belief: 1.00)
   - → supports: ha20_atomic_accuracy

## RFdiffusion outperforms RF Hallucination

29. **Alternative: benchmark artifact for unconditional generation** (prior: 0.15 → belief: 0.16)
   - → supports: comprehensive_improvement

30. **Alternative: easy benchmark set** (prior: 0.20 → belief: 0.21)
   - → supports: comprehensive_improvement

31. **Alternative: success due to AF2 filtering alone** (prior: 0.25 → belief: 0.26)
   - → supports: comprehensive_improvement

32. **RFdiffusion outperforms RF Hallucination** (prior: 0.92 → belief: 1.00)
   - → supports: comprehensive_improvement

## High in silico success for symmetric oligomers

33. **19% binder success rate — 100× improvement over Rosetta ★** (prior: 0.50 → belief: 1.00)
   - ← infer(alt_copying_pdb_interfaces, alt_nonspecific_adhesion, binder_specificity, ddpm_properties_for_protein_design, denoising_process, novel_interfaces, pretraining_benefit, previous_binder_design_limitations, prior_ddpm_limitations, rf_inpainting_limitations, self_conditioning_improvement, two_orders_attribution) [0.43 bits]
   - → supports: comprehensive_improvement, ha20_atomic_accuracy

34. **RFdiffusion solves 23/25 benchmark problems ★** (prior: 0.50 → belief: 1.00)
   - ← infer(alt_memorization, alt_noise_free_overfitting, alt_nonspecific_binding_p53_mdm2, ddpm_properties_for_protein_design, denoising_process, hallucination_benchmark, motif_not_from_training, noise_free_reverse, p53_mdm2_design, pretraining_benefit, prior_ddpm_limitations, rf_inpainting_benchmark, rf_inpainting_limitations, self_conditioning_improvement) [0.25 bits]
   - → supports: comprehensive_improvement

35. **High in silico success for symmetric oligomers ★** (prior: 0.50 → belief: 1.00)
   - ← infer(alt_coincidental_sec_profiles, alt_disordered_aggregates_mimicking_icosahedral, alt_structural_mimicry_in_nsem, ddpm_properties_for_protein_design, denoising_process, icosahedral_he0902, nsem_validates_cyclic, pretraining_benefit, prior_ddpm_limitations, rf_inpainting_limitations, sec_validation_oligomers, self_conditioning_improvement) [0.05 bits]

## RFdiffusion is comprehensive improvement over prior methods

36. **RFdiffusion achieves atomic-level accuracy in binder design ★** (prior: 0.50 → belief: 0.87)
   - ← infer(alt_ha20_alternative_conformation, binder_success_rate, ha20_cryoem_structure) [0.76 bits]
   - → supports: rfdiffusion_broad_success

37. **RFdiffusion is comprehensive improvement over prior methods ★** (prior: 0.50 → belief: 0.99)
   - ← infer(alt_benchmark_other_explanation, alt_binder_other_explanation, alt_outperforms_other_explanation, binder_success_rate, outperforms_hallucination, rfdiffusion_benchmark_performance) [0.68 bits]
   - → supports: rfdiffusion_broad_success

## RFdiffusion achieves broad design success

38. **RFdiffusion achieves broad design success ★** (prior: 0.50 → belief: 0.76)
   - ← infer(comprehensive_improvement, ha20_atomic_accuracy) [0.61 bits]
   - → supports: generality_claim

## RFdiffusion enables protein design from minimal specifications

39. **RFdiffusion enables protein design from minimal specifications ★** (prior: 0.50 → belief: 0.61)
   - ← infer(rfdiffusion_broad_success) [0.60 bits]
