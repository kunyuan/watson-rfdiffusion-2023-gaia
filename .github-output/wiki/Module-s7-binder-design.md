# Module: s7_binder_design

### binder_design_approach

**QID:** `github:watson_rfdiffusion_2023::binder_design_approach`
**Type:** setting
**Role:** setting
**Content:** For binder design, RFdiffusion was fine-tuned on protein complex structures, with a feature indicating a subset of residues on the target chain ('interface hotspot residues') to which the diffused chain binds. An additional model was fine-tuned to condition binder diffusion on secondary structure and block-adjacency information for coarse-grained topology control, in addition to interface hotspots.

### binder_filtering

**QID:** `github:watson_rfdiffusion_2023::binder_filtering`
**Type:** setting
**Role:** setting
**Content:** Designed binders were filtered by AF2 confidence in the interface and monomer structure, and 95 designs were selected per target for experimental characterization.

### previous_binder_design_limitations

**QID:** `github:watson_rfdiffusion_2023::previous_binder_design_limitations`
**Type:** claim
**Role:** independent
**Content:** The previous Rosetta-based method for de novo binder design from target structure information alone required testing tens of thousands of designs (many thousands screened per campaign) with low experimental success rates, and relied on prespecifying particular protein scaffolds, limiting diversity and shape complementarity. No deep-learning method had previously demonstrated experimental general success in designing completely de novo binders.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::binder_success_rate`

### binder_success_rate

**QID:** `github:watson_rfdiffusion_2023::binder_success_rate`
**Type:** claim
**Role:** derived
**Content:** The overall experimental success rate for RFdiffusion binders (binding at or above 50% of maximal BLI response for positive control at 10 μM) was 19% across five targets, an increase of roughly two orders of magnitude over the previous Rosetta-based method on the same targets. Binders were identified for all five targets with fewer than 100 designs tested per target.
**Belief:** 1.00
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::pipeline_description`, `github:watson_rfdiffusion_2023::previous_binder_design_limitations`, `github:watson_rfdiffusion_2023::two_orders_attribution`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::novel_interfaces`, `github:watson_rfdiffusion_2023::alt_copying_pdb_interfaces`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::binder_specificity`, `github:watson_rfdiffusion_2023::alt_nonspecific_adhesion`
**figure:** artifacts/images/85f56f116ef86862c9d2617c2f79cb30058fd9d1d78fca17d1e510650cb79fed.jpg
**caption:** Fig. 6 | De novo design of protein-binding proteins. Binder design for 5 targets, BLI titrations, HA_20 cryo-EM structure at 2.9 Å.
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::binder_targets_and_affinities`; noisy_and -> `github:watson_rfdiffusion_2023::ha20_atomic_accuracy`; abduction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`; induction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`

### binder_targets_and_affinities

**QID:** `github:watson_rfdiffusion_2023::binder_targets_and_affinities`
**Type:** claim
**Role:** derived
**Content:** De novo binders were designed against five targets: Influenza A H1 Haemagglutinin (HA), Interleukin-7 Receptor-α (IL-7Rα), Programmed Death-Ligand 1 (PD-L1), Insulin Receptor (InsR), and Tropomyosin Receptor Kinase A (TrkA). Full BLI titrations showed nanomolar affinities with no further experimental optimization, including HA and IL-7Rα binders with affinities of ~30 nM.
**Belief:** 0.92
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::binder_success_rate`
**figure:** artifacts/images/85f56f116ef86862c9d2617c2f79cb30058fd9d1d78fca17d1e510650cb79fed.jpg
**caption:** Fig. 6 | De novo design of protein-binding proteins. Binder design for 5 targets, BLI titrations, HA_20 cryo-EM structure at 2.9 Å.

### two_orders_attribution

**QID:** `github:watson_rfdiffusion_2023::two_orders_attribution`
**Type:** claim
**Role:** independent
**Content:** The two-orders-of-magnitude improvement in binder design success rate is attributed approximately one order of magnitude to RFdiffusion itself (better backbone generation) and the second order of magnitude to filtering with AF2 (better design selection).
**Prior:** 0.75
**Belief:** 1.00
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::binder_success_rate`

### binder_specificity

**QID:** `github:watson_rfdiffusion_2023::binder_specificity`
**Type:** claim
**Role:** independent
**Content:** Six of the highest affinity IL-7Rα binders were assessed by competition BLI, and all six competed for binding with a structurally validated positive control binding to the same site, indicating site-specific binding.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::binder_success_rate`

### novel_interfaces

**QID:** `github:watson_rfdiffusion_2023::novel_interfaces`
**Type:** claim
**Role:** independent
**Content:** Binding interfaces designed by RFdiffusion were often highly distinct from interfaces to these targets found in the PDB.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::binder_success_rate`

### ha20_cryoem_structure

**QID:** `github:watson_rfdiffusion_2023::ha20_cryoem_structure`
**Type:** claim
**Role:** independent
**Content:** The cryo-EM structure of the highest affinity Influenza binder (HA_20, Kd = 28 nM) in complex with Iowa43 HA was solved at 2.9 Å resolution. 3D heterogeneous refinement without symmetry revealed full occupancy of all three HA stem epitopes by HA_20.
**Prior:** 0.95
**Belief:** 1.00
**figure:** artifacts/images/85f56f116ef86862c9d2617c2f79cb30058fd9d1d78fca17d1e510650cb79fed.jpg
**caption:** Fig. 6 | De novo design of protein-binding proteins. Binder design for 5 targets, BLI titrations, HA_20 cryo-EM structure at 2.9 Å.
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ha20_matches_design`

### ha20_matches_design

**QID:** `github:watson_rfdiffusion_2023::ha20_matches_design`
**Type:** claim
**Role:** derived
**Content:** The cryo-EM 3D structure of the HA_20-HA complex almost perfectly matches the computational design model with 0.63 Å backbone r.m.s.d. Over the binder alone, the experimental structure deviates from the RFdiffusion design by only 0.6 Å.
**Belief:** 0.95
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::ha20_cryoem_structure`, `github:watson_rfdiffusion_2023::alt_ha20_alternative_conformation`
**figure:** artifacts/images/85f56f116ef86862c9d2617c2f79cb30058fd9d1d78fca17d1e510650cb79fed.jpg
**caption:** Fig. 6 | De novo design of protein-binding proteins. Binder design for 5 targets, BLI titrations, HA_20 cryo-EM structure at 2.9 Å.
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::ha20_atomic_accuracy`

### ha20_atomic_accuracy

**QID:** `github:watson_rfdiffusion_2023::ha20_atomic_accuracy`
**Type:** claim
**Role:** derived
**Content:** The near-perfect agreement between the cryo-EM structure and the RFdiffusion design model (0.63 Å r.m.s.d.) demonstrates that RFdiffusion can design functional proteins with atomic-level accuracy and precisely target functionally relevant sites on therapeutically important proteins.
**Belief:** 0.87
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::ha20_matches_design`, `github:watson_rfdiffusion_2023::binder_success_rate`
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::rfdiffusion_broad_success`

### alt_copying_pdb_interfaces

**QID:** `github:watson_rfdiffusion_2023::alt_copying_pdb_interfaces`
**Type:** claim
**Role:** independent
**Content:** The high binder success rate could be due to RFdiffusion recapitulating known binding modes from the PDB training set rather than generating genuinely new protein-protein interfaces.
**Prior:** 0.15
**Belief:** 0.15
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::binder_success_rate`

### alt_nonspecific_adhesion

**QID:** `github:watson_rfdiffusion_2023::alt_nonspecific_adhesion`
**Type:** claim
**Role:** independent
**Content:** The binders could achieve high BLI signals through non-specific adhesion to the target surface rather than site-specific binding at the designed interface.
**Prior:** 0.18
**Belief:** 0.18
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::binder_success_rate`

### alt_ha20_alternative_conformation

**QID:** `github:watson_rfdiffusion_2023::alt_ha20_alternative_conformation`
**Type:** claim
**Role:** independent
**Content:** The cryo-EM density could be fit to a different structural model that does not resemble the RFdiffusion design, indicating the binder adopted an alternative conformation.
**Prior:** 0.05
**Belief:** 0.10
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ha20_matches_design`
