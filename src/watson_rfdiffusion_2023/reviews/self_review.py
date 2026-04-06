"""Self-review sidecar: priors and conditional probabilities for Watson et al. 2023 RFdiffusion paper."""

from gaia.review import ReviewBundle, review_claim, review_strategy

from .. import (
    # --- Independent premise claims ---
    # Motivation
    ddpm_properties_for_protein_design,
    prior_ddpm_limitations,
    rf_inpainting_limitations,
    # Method
    denoising_process,
    self_conditioning_improvement,
    pretraining_benefit,
    mse_vs_fape_ablation,
    # Unconditional
    af2_validates_unconditional_designs,
    experimental_validation_monomers,
    fold_conditioned_generation,
    outperforms_hallucination,
    # Oligomers
    sec_validation_oligomers,
    nsem_validates_cyclic,
    icosahedral_he0902,
    # Motif scaffolding
    hallucination_benchmark,
    rf_inpainting_benchmark,
    p53_mdm2_design,
    # Symmetric motif
    ni_binding_experimental,
    ni_binding_histidine_dependence,
    ni_binding_nsem,
    # Binder design
    previous_binder_design_limitations,
    two_orders_attribution,
    binder_specificity,
    ha20_cryoem_structure,
    # Orphaned claims
    future_nucleic_acids,
    future_ligands,
    motif_not_from_training,
    ni_binding_endothermic,
    noise_free_reverse,
    novel_interfaces,
    retroaldolase_demonstration,
    # Alternative explanations
    alt_nonspecific_folding,
    alt_coincidental_sec_profiles,
    alt_structural_mimicry_in_nsem,
    alt_disordered_aggregates_mimicking_icosahedral,
    alt_nonspecific_binding_p53_mdm2,
    alt_nonspecific_metal_chelation,
    alt_indirect_structural_disruption_h52a,
    alt_alternative_c4_arrangement,
    alt_nonspecific_adhesion,
    alt_ha20_alternative_conformation,
    alt_memorization,
    alt_copying_pdb_interfaces,
    # Induction alternatives (s5)
    alt_noise_free_overfitting,
    # Induction alternatives (s8)
    alt_outperforms_other_explanation,
    alt_benchmark_other_explanation,
    alt_binder_other_explanation,
    alt_ideality_exp_artifact,
    alt_ideality_fold_artifact,
    alt_af2_coincidence,
    alt_uniform_nonspecific_mechanism,
    # --- Strategies ---
    _strat_key_insight,
    _strat_mse_loss,
    _strat_ablation,
    _strat_pipeline,
    _strat_af2_validates,
    _strat_compute,
    _strat_symmetric_success,
    _strat_novel_topologies,
    _strat_expanded_tim,
    _strat_dihedral,
    _strat_benchmark,
    _strat_benchmark_support,
    _strat_p53_affinity,
    _strat_enzyme,
    _strat_ni_endothermic,
    _strat_sars_cov2,
    _strat_ni_design,
    _strat_novel_interfaces,
    _strat_binder_success,
    _strat_binder_affinities,
    _strat_atomic_accuracy,
    _strat_comprehensive,
    _strat_ideality,
    _strat_broad_success,
    _strat_generality,
)


REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ============================================================
        # INDEPENDENT PREMISES
        # ============================================================

        # -- Motivation --
        review_claim(ddpm_properties_for_protein_design, prior=0.90,
            judgment="supporting",
            justification="Well-established DDPM properties demonstrated in image generation and adapted for proteins."),
        review_claim(prior_ddpm_limitations, prior=0.85,
            judgment="supporting",
            justification="Documented in multiple papers (Trippe et al., Anand & Achim). No experimental validation reported."),
        review_claim(rf_inpainting_limitations, prior=0.85,
            judgment="supporting",
            justification="Determinism and failure on minimal sites documented by Wang et al. 2022."),

        # -- Method --
        review_claim(denoising_process, prior=0.92,
            judgment="supporting",
            justification="Standard DDPM procedure adapted for protein frames. Mathematically well-defined."),
        review_claim(self_conditioning_improvement, prior=0.88,
            judgment="supporting",
            justification="Ablation study (Extended Data Fig. 1e) directly shows improvement. Consistent with AF2 recycling success."),
        review_claim(pretraining_benefit, prior=0.88,
            judgment="supporting",
            justification="Controlled ablation (Extended Data Fig. 1f,g): pretrained vs random init. Clear benefit."),
        review_claim(mse_vs_fape_ablation, prior=0.88,
            judgment="supporting",
            justification="Direct ablation (Extended Data Fig. 1d) confirms MSE is crucial for unconditional generation."),

        # -- Unconditional --
        review_claim(af2_validates_unconditional_designs, prior=0.92,
            judgment="supporting",
            justification="AF2 and ESMFold predictions closely matching designs up to 600 residues is direct computational evidence."),
        review_claim(experimental_validation_monomers, prior=0.92,
            judgment="supporting",
            justification="CD spectra and thermostability for 9 designs are direct experimental measurements."),
        review_claim(fold_conditioned_generation, prior=0.88,
            judgment="supporting",
            justification="42.5% TIM barrel + 54.1% NTF2 success, plus 8/11 TIM barrel experimental validation."),
        review_claim(outperforms_hallucination, prior=0.92,
            judgment="supporting",
            justification="Direct statistical comparison: z = 9.5, P = 1.6 × 10⁻²¹. Extremely strong evidence."),

        # -- Oligomers --
        review_claim(sec_validation_oligomers, prior=0.92,
            judgment="supporting",
            justification="SEC data for 608 designs with 87-126 hits. Standard experimental methodology."),
        review_claim(nsem_validates_cyclic, prior=0.92,
            judgment="supporting",
            justification="nsEM 2D class averages and 3D reconstructions across multiple symmetries. Direct structural evidence."),
        review_claim(icosahedral_he0902, prior=0.88,
            judgment="supporting",
            justification="Single icosahedral success out of 48, but nsEM 3D reconstruction closely matches design."),

        # -- Motif scaffolding --
        review_claim(hallucination_benchmark, prior=0.88,
            judgment="supporting",
            justification="15/25 success for Hallucination on standardized benchmark. Reproduced from published methods."),
        review_claim(rf_inpainting_benchmark, prior=0.88,
            judgment="supporting",
            justification="19/25 success for RFjoint Inpainting. Reproduced from published methods."),
        review_claim(p53_mdm2_design, prior=0.92,
            judgment="supporting",
            justification="55/96 designs showing binding at 10 μM. Direct BLI screening result."),

        # -- Symmetric motif --
        review_claim(ni_binding_experimental, prior=0.92,
            judgment="supporting",
            justification="ITC measurements: 18/36 bind Ni²⁺ with correct 1:4 stoichiometry. Quantitative data."),
        review_claim(ni_binding_histidine_dependence, prior=0.92,
            judgment="supporting",
            justification="H52A abolishes binding in 17/17 cases. Strong controlled experiment."),
        review_claim(ni_binding_nsem, prior=0.88,
            judgment="supporting",
            justification="nsEM 2D class averages and NiB1.17 3D reconstruction showing C4 symmetry."),

        # -- Binder design --
        review_claim(previous_binder_design_limitations, prior=0.88,
            judgment="supporting",
            justification="Rosetta binder design limitations documented by Cao et al. 2022."),
        review_claim(two_orders_attribution, prior=0.75,
            judgment="tentative",
            justification="~10× RFdiffusion + ~10× AF2 filtering is authors' estimate. Reasonable but approximate."),
        review_claim(binder_specificity, prior=0.88,
            judgment="supporting",
            justification="6/6 IL-7Rα binders competing with positive control. Direct competition BLI evidence."),
        review_claim(ha20_cryoem_structure, prior=0.95,
            judgment="supporting",
            justification="2.9 Å cryo-EM with full occupancy. High-quality structural determination."),

        # ============================================================
        # ORPHANED CLAIMS
        # ============================================================

        review_claim(future_nucleic_acids, prior=0.70,
            judgment="tentative",
            justification="RoseTTAFoldNA exists so extension is plausible but not demonstrated."),
        review_claim(future_ligands, prior=0.65,
            judgment="tentative",
            justification="RF extension to ligands plausible but not yet demonstrated."),
        review_claim(motif_not_from_training, prior=0.88,
            judgment="supporting",
            justification="Analysis in Supplementary Fig. 7 directly shows this."),
        review_claim(ni_binding_endothermic, prior=0.88,
            judgment="supporting",
            justification="ITC data directly shows endothermic binding for specific designs."),
        review_claim(noise_free_reverse, prior=0.88,
            judgment="supporting",
            justification="17/23 problems improved. Direct computational observation."),
        review_claim(novel_interfaces, prior=0.88,
            judgment="supporting",
            justification="Structural comparison to PDB interfaces. Direct computational analysis."),
        review_claim(retroaldolase_demonstration, prior=0.80,
            judgment="supporting",
            justification="In silico demonstration only, no experimental validation."),

        # ============================================================
        # ALTERNATIVE EXPLANATIONS — pi(Alt) = explanatory power
        # ============================================================

        review_claim(alt_nonspecific_folding, prior=0.20,
            judgment="opposing",
            justification="Non-specific aggregation cannot explain CD spectra matching designed topologies across 9 designs."),
        review_claim(alt_coincidental_sec_profiles, prior=0.30,
            judgment="opposing",
            justification="Some coincidence plausible individually, but systematic agreement across 87+ designs unlikely."),
        review_claim(alt_structural_mimicry_in_nsem, prior=0.12,
            judgment="opposing",
            justification="Different structure matching 2D classes, 3D reconstruction, and pinwheel shape at multiple orientations: extremely unlikely."),
        review_claim(alt_disordered_aggregates_mimicking_icosahedral, prior=0.08,
            judgment="opposing",
            justification="Disordered aggregates cannot produce triangular hubs around C5 axes."),
        review_claim(alt_nonspecific_binding_p53_mdm2, prior=0.18,
            judgment="opposing",
            justification="Non-specific binding cannot explain both 55/96 hit rate AND sub-nM affinities."),
        review_claim(alt_nonspecific_metal_chelation, prior=0.22,
            judgment="opposing",
            justification="Non-specific chelation cannot explain precise 1:4 stoichiometry."),
        review_claim(alt_indirect_structural_disruption_h52a, prior=0.12,
            judgment="opposing",
            justification="Indirect disruption in 17/17 different scaffolds by conservative Ala mutation: extremely unlikely."),
        review_claim(alt_alternative_c4_arrangement, prior=0.12,
            judgment="opposing",
            justification="Alternative C4 matching design model AND showing His-dependent binding: extremely unlikely."),
        review_claim(alt_nonspecific_adhesion, prior=0.18,
            judgment="opposing",
            justification="Non-specific adhesion cannot explain competition with validated positive control at same site."),
        review_claim(alt_ha20_alternative_conformation, prior=0.05,
            judgment="opposing",
            justification="At 2.9 Å with 0.63 Å r.m.s.d. to design, alternative conformation virtually impossible."),
        review_claim(alt_memorization, prior=0.15,
            judgment="opposing",
            justification="Directly contradicted by Supplementary Fig. 7 showing no correlation with training set."),
        review_claim(alt_copying_pdb_interfaces, prior=0.15,
            judgment="opposing",
            justification="Directly contradicted by structural analysis showing novel interfaces distinct from PDB."),

        # ============================================================
        # INDUCTION ALTERNATIVES — explicit alt_exps
        # ============================================================

        # _strat_comprehensive alternatives
        review_claim(alt_outperforms_other_explanation, prior=0.15,
            judgment="opposing",
            justification="Benchmark artifact cannot explain z=9.5 (P=1.6e-21) across 400 designs per condition."),
        review_claim(alt_benchmark_other_explanation, prior=0.20,
            judgment="opposing",
            justification="23/25 from 6 publications across diverse problem types; unlikely to be uniformly easy."),
        review_claim(alt_binder_other_explanation, prior=0.25,
            judgment="tentative",
            justification="AF2 filtering contributes ~10×, but RFdiffusion also contributes ~10×; partially valid."),

        # _strat_ideality alternatives
        review_claim(alt_ideality_exp_artifact, prior=0.25,
            judgment="opposing",
            justification="Non-specific stability is possible but CD spectra specifically match designed topologies."),
        review_claim(alt_ideality_fold_artifact, prior=0.30,
            judgment="tentative",
            justification="TIM barrel inherent stability is partially valid; 8/11 success partly reflects fold robustness."),

        # _strat_benchmark_support alternatives
        review_claim(alt_noise_free_overfitting, prior=0.20,
            judgment="opposing",
            justification="17/23 consistency across diverse problems argues against overfitting to benchmark."),
        # alt_training_correlation_artifact removed — merged into alt_memorization
        # to avoid double-counting motif_not_from_training evidence

        # ============================================================
        # STRATEGY PARAMETERS — conditional_probability for noisy_and
        # ============================================================

        review_strategy(_strat_key_insight, conditional_probability=0.85,
            judgment="formalized",
            justification="Creative but well-motivated reasoning from DDPM properties + RF capabilities."),
        review_strategy(_strat_mse_loss, conditional_probability=0.90,
            judgment="formalized",
            justification="Key insight + ablation → MSE design. Ablation directly confirms."),
        review_strategy(_strat_ablation, conditional_probability=0.90,
            judgment="formalized",
            justification="Two independent ablation studies each directly confirm a design choice. Controlled experiments."),
        review_strategy(_strat_pipeline, conditional_probability=0.90,
            judgment="formalized",
            justification="Pipeline follows straightforwardly from method design."),
        # _strat_af2_validates is now abduction (no params needed)
        review_strategy(_strat_compute, conditional_probability=0.92,
            judgment="formalized",
            justification="Direct runtime comparison: 11s vs 8.5min. Straightforward benchmark."),
        review_strategy(_strat_symmetric_success, conditional_probability=0.85,
            judgment="formalized",
            justification="Extension to symmetry leverages equivariance. Success with auxiliary potential."),
        review_strategy(_strat_novel_topologies, conditional_probability=0.92,
            judgment="formalized",
            justification="TM-align scores directly quantify novelty."),
        review_strategy(_strat_expanded_tim, conditional_probability=0.88,
            judgment="formalized",
            justification="nsEM reconstructions confirm structures."),
        review_strategy(_strat_dihedral, conditional_probability=0.88,
            judgment="formalized",
            justification="Multiple validation methods (SEC, nsEM, cryo-EM) provide converging evidence."),
        review_strategy(_strat_benchmark, conditional_probability=0.88,
            judgment="formalized",
            justification="Controlled comparison on same 25 problems with same metric."),
        # _strat_benchmark_support is induction (no direct params needed)
        review_strategy(_strat_p53_affinity, conditional_probability=0.88,
            judgment="formalized",
            justification="BLI titrations are quantitative. 1000× improvement over native peptide."),
        review_strategy(_strat_enzyme, conditional_probability=0.78,
            judgment="tentative",
            justification="In silico only, required fine-tuning. Retroaldolase demo adds support but still no wet-lab."),
        # _strat_ni_endothermic is now abduction (no params needed)
        review_strategy(_strat_sars_cov2, conditional_probability=0.88,
            judgment="formalized",
            justification="Combines two validated capabilities. AF2 confirms structural accuracy."),
        review_strategy(_strat_ni_design, conditional_probability=0.85,
            judgment="formalized",
            justification="Extends symmetric design to metal coordination. AF2-confirmed."),
        # _strat_novel_interfaces is now abduction (no params needed)
        review_strategy(_strat_binder_success, conditional_probability=0.88,
            judgment="formalized",
            justification="Direct experimental screening on 5 targets with clear improvement."),
        review_strategy(_strat_binder_affinities, conditional_probability=0.92,
            judgment="formalized",
            justification="BLI titrations with kinetic fitting. Reliable measurements."),
        review_strategy(_strat_atomic_accuracy, conditional_probability=0.92,
            judgment="formalized",
            justification="0.63 Å cryo-EM r.m.s.d. is definitive structural evidence."),
        # _strat_comprehensive is now induction (no direct params needed)
        # _strat_ideality is now induction (no direct params needed)
        review_strategy(_strat_broad_success, conditional_probability=0.88,
            judgment="formalized",
            justification="Comprehensive improvement + atomic validation → broad success."),
        review_strategy(_strat_generality, conditional_probability=0.80,
            judgment="tentative",
            justification="Broad success supports generality, but polar sites and ligands not yet tested."),

        # ============================================================
        # NEW ABDUCTION ALTERNATIVES
        # ============================================================

        review_claim(alt_af2_coincidence, prior=0.20,
            judgment="opposing",
            justification="Shared PDB bias is weakened by two independent predictors (AF2+ESMFold) and low TM-scores to PDB."),
        review_claim(alt_uniform_nonspecific_mechanism, prior=0.20,
            judgment="opposing",
            justification="Uniform non-specific mechanism would not produce thermodynamic diversity (exo- vs endothermic)."),

        # Derived claims: NO priors needed — inference engine defaults to 0.5,
        # beliefs determined entirely by BP propagation from leaf premises.
    ],
)
