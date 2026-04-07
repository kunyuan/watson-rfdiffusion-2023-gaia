# watson_rfdiffusion_2023

## Modules

- [motivation](Module-motivation) (11 nodes)
- [s2_method](Module-s2-method) (10 nodes)
- [s3_unconditional](Module-s3-unconditional) (7 nodes)
- [s4_oligomers](Module-s4-oligomers) (11 nodes)
- [s5_motif_scaffolding](Module-s5-motif-scaffolding) (14 nodes)
- [s6_symmetric_motif](Module-s6-symmetric-motif) (11 nodes)
- [s7_binder_design](Module-s7-binder-design) (14 nodes)
- [s8_discussion](Module-s8-discussion) (10 nodes)
- [Root](Module-Root) (0 nodes)

## Claim Index

| Label | Type | Module | Belief |
|-------|------|--------|--------|
| ddpm_definition | setting | motivation | — |
| rosettafold_definition | setting | motivation | — |
| alphafold2_definition | setting | motivation | — |
| proteinmpnn_definition | setting | motivation | — |
| protein_design_goal | setting | motivation | — |
| in_silico_success_definition | setting | motivation | — |
| ddpm_properties_for_protein_design | claim | motivation | 1.00 |
| prior_ddpm_limitations | claim | motivation | 1.00 |
| rf_inpainting_limitations | claim | motivation | 1.00 |
| key_insight | claim | motivation | 1.00 |
| rfdiffusion_broad_success | claim | motivation | 0.76 |
| pdb_training_data | setting | s2_method | — |
| frame_representation | setting | s2_method | — |
| mse_loss_design | claim | s2_method | 0.79 |
| denoising_process | claim | s2_method | 1.00 |
| self_conditioning_improvement | claim | s2_method | 1.00 |
| pretraining_benefit | claim | s2_method | 1.00 |
| mse_vs_fape_ablation | claim | s2_method | 0.88 |
| pipeline_description | claim | s2_method | 1.00 |
| compute_efficiency | claim | s2_method | 0.92 |
| method_design_validated | claim | s2_method | 1.00 |
| unconditional_generates_diverse_structures | claim | s3_unconditional | 0.96 |
| af2_validates_unconditional_designs | claim | s3_unconditional | 1.00 |
| experimental_validation_monomers | claim | s3_unconditional | 1.00 |
| outperforms_hallucination | claim | s3_unconditional | 1.00 |
| fold_conditioned_generation | claim | s3_unconditional | 1.00 |
| alt_af2_coincidence | claim | s3_unconditional | 0.23 |
| alt_nonspecific_folding | claim | s3_unconditional | 0.23 |
| symmetric_design_approach | setting | s4_oligomers | — |
| symmetric_high_success | claim | s4_oligomers | 1.00 |
| novel_oligomeric_topologies | claim | s4_oligomers | 0.92 |
| sec_validation_oligomers | claim | s4_oligomers | 1.00 |
| nsem_validates_cyclic | claim | s4_oligomers | 1.00 |
| expanded_tim_barrels | claim | s4_oligomers | 0.88 |
| dihedral_tetrahedral_icosahedral | claim | s4_oligomers | 0.88 |
| icosahedral_he0902 | claim | s4_oligomers | 1.00 |
| alt_coincidental_sec_profiles | claim | s4_oligomers | 0.30 |
| alt_structural_mimicry_in_nsem | claim | s4_oligomers | 0.12 |
| alt_disordered_aggregates_mimicking_icosahedral | claim | s4_oligomers | 0.08 |
| motif_scaffolding_definition | setting | s5_motif_scaffolding | — |
| benchmark_definition | setting | s5_motif_scaffolding | — |
| rfdiffusion_benchmark_performance | claim | s5_motif_scaffolding | 1.00 |
| hallucination_benchmark | claim | s5_motif_scaffolding | 1.00 |
| rf_inpainting_benchmark | claim | s5_motif_scaffolding | 1.00 |
| noise_free_reverse | claim | s5_motif_scaffolding | 1.00 |
| motif_not_from_training | claim | s5_motif_scaffolding | 1.00 |
| p53_mdm2_design | claim | s5_motif_scaffolding | 1.00 |
| p53_mdm2_affinity | claim | s5_motif_scaffolding | 0.88 |
| enzyme_scaffolding_success | claim | s5_motif_scaffolding | 0.62 |
| retroaldolase_demonstration | claim | s5_motif_scaffolding | 0.80 |
| alt_nonspecific_binding_p53_mdm2 | claim | s5_motif_scaffolding | 0.18 |
| alt_memorization | claim | s5_motif_scaffolding | 0.15 |
| alt_noise_free_overfitting | claim | s5_motif_scaffolding | 0.20 |
| metal_coordination_geometry | setting | s6_symmetric_motif | — |
| sars_cov2_trimeric_binder_design | claim | s6_symmetric_motif | 0.88 |
| ni_binding_design | claim | s6_symmetric_motif | 1.00 |
| ni_binding_experimental | claim | s6_symmetric_motif | 1.00 |
| ni_binding_histidine_dependence | claim | s6_symmetric_motif | 1.00 |
| ni_binding_nsem | claim | s6_symmetric_motif | 1.00 |
| ni_binding_endothermic | claim | s6_symmetric_motif | 1.00 |
| alt_uniform_nonspecific_mechanism | claim | s6_symmetric_motif | 0.20 |
| alt_nonspecific_metal_chelation | claim | s6_symmetric_motif | 0.22 |
| alt_indirect_structural_disruption_h52a | claim | s6_symmetric_motif | 0.12 |
| alt_alternative_c4_arrangement | claim | s6_symmetric_motif | 0.12 |
| binder_design_approach | setting | s7_binder_design | — |
| binder_filtering | setting | s7_binder_design | — |
| previous_binder_design_limitations | claim | s7_binder_design | 1.00 |
| binder_success_rate | claim | s7_binder_design | 1.00 |
| binder_targets_and_affinities | claim | s7_binder_design | 0.92 |
| two_orders_attribution | claim | s7_binder_design | 1.00 |
| binder_specificity | claim | s7_binder_design | 1.00 |
| novel_interfaces | claim | s7_binder_design | 1.00 |
| ha20_cryoem_structure | claim | s7_binder_design | 1.00 |
| ha20_matches_design | claim | s7_binder_design | 0.95 |
| ha20_atomic_accuracy | claim | s7_binder_design | 0.87 |
| alt_copying_pdb_interfaces | claim | s7_binder_design | 0.15 |
| alt_nonspecific_adhesion | claim | s7_binder_design | 0.18 |
| alt_ha20_alternative_conformation | claim | s7_binder_design | 0.10 |
| comprehensive_improvement | claim | s8_discussion | 0.99 |
| ideality_and_stability | claim | s8_discussion | 0.93 |
| generality_claim | claim | s8_discussion | 0.61 |
| future_nucleic_acids | claim | s8_discussion | 0.70 |
| future_ligands | claim | s8_discussion | 0.65 |
| alt_outperforms_other_explanation | claim | s8_discussion | 0.16 |
| alt_benchmark_other_explanation | claim | s8_discussion | 0.21 |
| alt_binder_other_explanation | claim | s8_discussion | 0.26 |
| alt_ideality_exp_artifact | claim | s8_discussion | 0.30 |
| alt_ideality_fold_artifact | claim | s8_discussion | 0.35 |
