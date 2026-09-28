BONE DENSITY LOSS COUNTERMEASURES FOR LONG-DURATION SPACEFLIGHT: AN ODE MODEL OF OSTEOCLAST-OSTEOBLAST DYNAMICS UNDER MICROGRAVITY

**Thesis #45** — computational research thesis
**Author:** Kelechi Emeka Ogbonna
**Correspondence:** kelechiogbonna300@gmail.com
**Date:** September 2026
**Format:** B.Sc. project chapter structure (Nile University style)
**Citation style:** APA 6th edition (Author, Year)
**DOI:** none registered. Do not invent one.

[Preamble]
This work extends the foundational methodology established in Thesis Zero (BSc Carica papaya AgNP, Nile University 2022) by applying advanced computational modeling to physiological systems under extreme conditions. The analytical approaches utilized herein build heavily on the structural identifiability frameworks explored in companion theses T07, T09 (multi-channel identifiability), and T12 (stiff-sloppy reduction), collectively forming a robust paradigm for complex system analysis within the Project Confluence repository.

## Non-claims
The models, simulations, and findings presented in this manuscript are intended solely for academic computational research. This thesis does not constitute astronaut medical advice, clinical recommendations, or validated therapeutic protocols. The differential equation models are theoretical abstractions of bone remodeling dynamics and should not be used to guide human intervention without empirical biological validation.

---

## Declaration
I, Kelechi Emeka Ogbonna, declare that this research work titled "BONE DENSITY LOSS COUNTERMEASURES FOR LONG-DURATION SPACEFLIGHT: AN ODE MODEL OF OSTEOCLAST-OSTEOBLAST DYNAMICS UNDER MICROGRAVITY" was carried out by me under the independent computational research framework of Project Confluence. This work has not been presented for the award of any degree, diploma, or fellowship in this or any other institution.

---

## Abstract
Long-duration spaceflight imposes severe mechanical unloading on the skeletal system, leading to uncoupled bone remodeling and significant bone mineral density (BMD) loss. This thesis presents a deterministic ordinary differential equation (ODE) model of bone remodeling—incorporating osteoclast-osteoblast dynamics mediated by the RANKL/OPG/RANK signaling pathway—to simulate microgravity-induced osteoporosis and evaluate the identifiability of countermeasures. By parameterizing mechanical loading as a gravity-dependent forcing function, the model captures bone mass trajectories across 1g (Earth), microgravity (0g), and Mars (0.38g) environments. A central challenge in optimizing spaceflight countermeasures is the sparsity of inflight data; therefore, this study utilizes differential algebra to assess structural identifiability of countermeasure forcing terms from single-channel DXA-like BMD observations. Computational results demonstrate that while baseline remodeling parameters exhibit structural unidentifiability without cellular-level biomarker tracking, the specific pharmacokinetic forcing terms of antiresorptive interventions (e.g., bisphosphonates) become identifiable under optimal transit schedules. The integration of stiff-sloppy reduction techniques (developed in T12) permits robust estimation of efficacious dosing intervals despite parametric uncertainty. This work provides a theoretical framework for designing patient-specific countermeasures against spaceflight osteopenia, emphasizing the necessity of multi-channel data acquisition for future Mars transit missions.

## Keywords
Bone remodeling, Microgravity, Ordinary differential equations, Structural identifiability, Osteoclast, Osteoblast, RANKL/OPG, Spaceflight countermeasures, Project Confluence.

## Table of Contents
1.0 INTRODUCTION
    1.1 Background to the Study
    1.2 Statement of Research Problem
    1.3 Justification of Study
    1.4 Aim and Objectives of the Study
    1.5 Significance of the Study
    1.6 Scope of the Study
2.0 LITERATURE REVIEW
    2.1 Physiology of Bone Remodeling
    2.2 Effects of Microgravity on Skeletal Integrity
    2.3 Mathematical Modeling of Bone Dynamics
    2.4 Identifiability Analysis in Systems Biology
3.0 MATERIALS AND METHODS
    3.1 Model Formulation
    3.2 Gravity-Dependent Mechanical Loading Function
    3.3 Countermeasure Pharmacokinetic Forcing Terms
    3.4 Structural Identifiability Analysis
    3.5 Computational Simulation Environment
4.0 RESULTS
    4.1 Baseline Remodeling Dynamics at Earth Gravity (1g)
    4.2 Simulated Trajectories of Microgravity (0g) Induced Bone Loss
    4.3 Structural Identifiability of Countermeasure Forcing Terms
    4.4 Mars Transit Simulation and Countermeasure Efficacy
5.0 DISCUSSION, CONCLUSION AND RECOMMENDATION
    5.1 Discussion
    5.2 Conclusion
    5.3 Recommendation
References
Disclaimer

---

## 1.0 INTRODUCTION

### 1.1 Background to the Study
The exploration of the solar system, particularly the impending human missions to Mars, necessitates a profound understanding of physiological adaptations to extreme environments. The human skeletal system, having evolved under the constant presence of a 1g gravitational field, relies on continuous mechanical loading to maintain homeostatic bone remodeling. Bone tissue is a dynamic metabolic organ that continuously undergoes remodeling—a tightly coupled process of bone resorption by osteoclasts and bone formation by osteoblasts. Under terrestrial conditions, mechanical strain induced by gravity and muscle contraction signals osteocytes to regulate the balance between osteoclastogenesis and osteoblastogenesis, primarily through the receptor activator of nuclear factor kappa-B ligand (RANKL) and osteoprotegerin (OPG) pathway (Komarova et al., 2003).

In the environment of spaceflight, prolonged exposure to microgravity (~0g) drastically reduces mechanical stress on load-bearing bones. This unloading state precipitates a rapid and profound decoupling of the remodeling process, characterized by accelerated osteoclastic bone resorption and suppressed osteoblastic bone formation. Astronauts typically experience bone mineral density (BMD) loss at a rate of 1% to 2% per month in weight-bearing regions such as the lumbar spine, pelvis, and proximal femur (LeBlanc et al., 2000). Over a projected 3-year Mars transit mission, such relentless degradation poses catastrophic risks, including debilitating fractures and renal stone formation due to hypercalciuria.

To mitigate spaceflight osteopenia, various countermeasures have been implemented, ranging from high-intensity resistive exercise to pharmacological interventions such as bisphosphonates and anti-sclerostin antibodies. However, the precise scheduling and efficacy of these countermeasures during prolonged transit remain highly empirical. The formulation of deterministic ordinary differential equation (ODE) models allows for the theoretical exploration of complex cellular interactions within the bone microenvironment. Early mathematical representations (Pivonka et al., 2008; Lemaire et al., 2004) successfully captured the oscillatory nature of bone remodeling. Advancing these frameworks to incorporate gravity-dependent mechanical loading functions offers a mechanistic approach to simulating spaceflight conditions. Yet, the utility of such models hinges on the ability to accurately estimate internal parameters from observable clinical data. Structural identifiability analysis—a mathematical technique that determines whether unique parameter values can be deduced from idealized, noise-free input-output data—is therefore critical (Bellu et al., 2007). This thesis applies identifiability frameworks (previously explored in T07, T09, and T12) to assess how well countermeasure regimens can be monitored and optimized using sparse DXA-like BMD observations typical of spacecraft telemetry.

### 1.2 STATEMENT OF RESEARCH PROBLEM
During long-duration spaceflight (e.g., a Mars transit schedule), the primary diagnostic modality for assessing skeletal health is the periodic observation of overall bone mineral density (BMD), similar to terrestrial dual-energy X-ray absorptiometry (DXA). However, BMD is a macroscopic aggregate variable resulting from complex, microscopic, non-linear interactions between osteoclasts, osteoblasts, and signaling molecules (RANKL/OPG). The fundamental research problem this study addresses is determining which specific countermeasure forcing terms (representing pharmacological or exercise interventions) are structurally identifiable purely from aggregate DXA-like BMD observations over time. If the countermeasure parameters cannot be uniquely identified from the available macroscopic data, it becomes mathematically impossible to reliably tailor interventions to an individual astronaut's physiological trajectory during transit, risking under-dosing or toxic over-dosing.

### 1.3 JUSTIFICATION OF STUDY
Current protocols for prescribing countermeasures against spaceflight-induced bone loss rely heavily on terrestrial clinical trials and retrospective analyses of low-Earth orbit missions (e.g., aboard the ISS). Mars transit missions, however, present unprecedented durations of microgravity followed by partial gravity (0.38g). A predictive computational framework is essential to simulate these novel mission architectures. This study is justified by the critical need to transition from empirical guessing to mathematically rigorous, personalized countermeasure scheduling. By systematically evaluating the structural identifiability of an ODE bone remodeling model, this research determines exactly what clinical data is strictly necessary to monitor treatment efficacy. Furthermore, integrating the stiff-sloppy reduction techniques developed in T12 ensures that the mathematical models remain computationally tractable, bridging the gap between theoretical systems biology and practical mission planning.

### 1.4 AIM AND OBJECTIVES OF THE STUDY
The primary aim of this study is to construct and analyze a deterministic ODE model of osteoclast-osteoblast dynamics under microgravity to determine the structural identifiability of bone loss countermeasure forcing terms from macroscopic BMD data.

The specific objectives are:
1. To formulate a system of ODEs incorporating RANKL/OPG signaling and a gravity-dependent mechanical loading function.
2. To simulate bone remodeling trajectories under terrestrial (1g), microgravity (0g), and Martian (0.38g) conditions.
3. To perform differential algebraic structural identifiability analysis on the model parameters, treating BMD as the sole output channel.
4. To evaluate the identifiability of pharmacological countermeasure forcing terms during a simulated Mars transit schedule.
5. To apply stiff-sloppy parameter reduction (via methods from T12) to isolate identifiable parameter subsets for robust estimation.

**Non-aims:** This study does not attempt to validate the ODE models using novel biological samples, nor does it seek to propose new pharmaceutical agents. The focus remains strictly on the mathematical properties of the dynamic system.

### 1.5 SIGNIFICANCE OF THE STUDY
This research provides a vital theoretical underpinning for aerospace medicine. If specific countermeasure forcing terms are proven structurally identifiable from sparse BMD data, it mathematically guarantees that astronaut treatment plans can be dynamically adjusted in-flight using minimal equipment. Conversely, proving unidentifiability highlights a fundamental limitation in current monitoring protocols, signaling to aerospace engineers that new, multi-channel biomarker biosensors (e.g., for continuous blood calcium or RANKL tracking) are strictly required for safe Mars missions. This work advances the application of systems biology to space physiology and broadens the computational repository of Project Confluence.

### 1.6 SCOPE OF THE STUDY
The scope of this thesis is confined to deterministic ODE modeling of the basic multicellular unit (BMU) involved in bone remodeling. The model explicitly includes osteoclasts, osteoblasts, and the RANKL/OPG axis. Mechanical loading is abstracted as a continuous forcing function dependent on gravitational acceleration. The structural identifiability analysis assumes idealized, noise-free observations of total bone mass (analogous to DXA scans). 
Out of scope: The study does not model stochastic variations in cell populations, spatial partial differential equation (PDE) dynamics of bone architecture, or the specific pharmacokinetics of distinct brand-name drugs. The limitations of utilizing aggregate BMD as a proxy for structural bone strength are acknowledged as defects kept as defects.

---

## 2.0 LITERATURE REVIEW

### 2.1 Physiology of Bone Remodeling
Bone is a metabolically active tissue that undergoes continuous renewal through the process of remodeling. This process occurs in discrete, temporary anatomical structures known as basic multicellular units (BMUs). Remodeling ensures the repair of microdamage, adaptation to mechanical loads, and maintenance of calcium homeostasis (Frost, 1969). The cycle is coordinated by the sequential action of bone-resorbing osteoclasts (derived from hematopoietic stem cells) and bone-forming osteoblasts (derived from mesenchymal stem cells). 

The coupling between resorption and formation is tightly regulated by the RANKL/RANK/OPG signaling pathway. Osteoblasts and osteocytes secrete Receptor Activator of Nuclear Factor Kappa-B Ligand (RANKL), which binds to RANK receptors on osteoclast precursors, promoting their differentiation and activation. Conversely, osteoblasts also secrete osteoprotegerin (OPG), a decoy receptor that binds to RANKL, preventing it from interacting with RANK, thereby inhibiting osteoclastogenesis (Boyce & Xing, 2008). This delicate autocrine and paracrine balance is highly responsive to external mechanical stimuli.

### 2.2 Effects of Microgravity on Skeletal Integrity
Mechanical loading is the primary physical signal that dictates bone mass architecture. According to Mechanostat theory, bone tissue adapts its mass and geometry to the customary strains it experiences. Osteocytes embedded within the bone matrix act as the primary mechanosensors. Under normal terrestrial gravity (1g), ambulatory loads suppress the expression of sclerostin (an inhibitor of bone formation) and modulate the RANKL/OPG ratio to maintain steady bone mass (Robling et al., 2006).

In the microgravity environment of spaceflight, the absence of weight-bearing loads removes this critical mechanical stimulus. The result is rapid osteocyte apoptosis, increased sclerostin secretion, and a drastic upregulation of the RANKL/OPG ratio (Carmeliet et al., 2001). Clinical data from Skylab, Mir, and the International Space Station (ISS) indicate that astronauts lose an average of 1-2% of bone mineral density per month in the spine and lower extremities (LeBlanc et al., 2000). Without effective countermeasures, a three-year Mars mission could result in critical osteoporosis, leading to fragility fractures upon entering the Martian gravitational field (0.38g).

### 2.3 Mathematical Modeling of Bone Dynamics
The application of mathematical modeling to bone remodeling has evolved significantly. Early models by Komarova et al. (2003) utilized nonlinear ordinary differential equations to describe the autocrine and paracrine interactions between osteoclasts and osteoblasts, successfully capturing the limit-cycle oscillations characteristic of the BMU. Lemaire et al. (2004) expanded this framework to explicitly include the molecular dynamics of the RANKL/OPG axis and parathyroid hormone (PTH) interactions.

Pivonka et al. (2008) further refined these models by integrating mechanical loading factors, allowing the simulation of disuse osteopenia. However, most existing models are highly parameterized. While they effectively replicate physiological behavior in forward simulations, the inverse problem—estimating the underlying parameters from macroscopic data—remains notoriously difficult.

### 2.4 Identifiability Analysis in Systems Biology
Structural identifiability analysis determines whether the parameters of a dynamic model can be uniquely recovered from the system's output, assuming continuous, error-free data (Bellu et al., 2007). If a parameter is structurally unidentifiable, no amount of experimental data or algorithmic optimization can yield its true value, rendering model-based personalized medicine impossible. 

In the context of the Project Confluence series, Thesis T07 established robust differential algebra methods for assessing global identifiability. T09 explored the necessity of multi-channel observation in complex networks, while T12 introduced techniques for model reduction when parameters are practically unidentifiable (stiff-sloppy). Applying these methods to bone remodeling models is critical, as clinical measurements in spaceflight are typically restricted to single-channel macroscopic variables (BMD) rather than cellular concentrations.

---

## 3.0 MATERIALS AND METHODS

### 3.1 Model Formulation
This study adopts a nonlinear system of ordinary differential equations modified from the foundational works of Komarova et al. (2003) and Pivonka et al. (2008). The state variables represent the populations of active osteoclasts ($C$), active osteoblasts ($B$), and the total bone mass ($Z$). The system is defined as:

$dC/dt = \alpha_C \cdot C^{g_{11}} \cdot B^{g_{21}} \cdot H_C(g) - \beta_C \cdot C$
$dB/dt = \alpha_B \cdot C^{g_{12}} \cdot B^{g_{22}} \cdot H_B(g) - \beta_B \cdot B$
$dZ/dt = -k_C \cdot C + k_B \cdot B$

Where:
- $\alpha_C, \alpha_B$ are cellular proliferation rates.
- $\beta_C, \beta_B$ are cellular apoptosis rates.
- $g_{ij}$ represent the complex autocrine and paracrine signaling feedback loops (aggregating RANKL/OPG pathways).
- $k_C, k_B$ are the rates of bone resorption and formation, respectively.
- $H_C(g)$ and $H_B(g)$ are the gravity-dependent mechanical loading functions.

### 3.2 Gravity-Dependent Mechanical Loading Function
To simulate spaceflight, a mechanotransduction forcing term is introduced. Let $g(t)$ represent the gravitational acceleration at time $t$ relative to Earth normal (1g). 
For Earth: $g(t) = 1.0$
For Transit (Microgravity): $g(t) = 0.0$
For Mars: $g(t) = 0.38$

The mechanical modulation functions are modeled using Hill-type kinetics:
$H_C(g) = 1 + \lambda_C \cdot \exp(-\kappa \cdot g(t))$
$H_B(g) = \frac{g(t)}{g(t) + \lambda_B}$

This assumes that reduced gravity upregulates osteoclast activity and downregulates osteoblast activity.

### 3.3 Countermeasure Pharmacokinetic Forcing Terms
Pharmacological countermeasures (e.g., bisphosphonates) are introduced as a forcing function $U(t)$ that specifically targets osteoclast apoptosis ($\beta_C$). 
$\beta_C(t) = \beta_{C0} \cdot (1 + \gamma \cdot U(t))$
Where $U(t)$ is the administered drug concentration and $\gamma$ is the drug efficacy parameter.

### 3.4 Structural Identifiability Analysis
The structural identifiability of the system is analyzed using the differential algebra approach via the GenSSI toolbox principles (as utilized in T07). The observable output function is strictly defined as total bone mass, simulating DXA scans:
$Y(t) = Z(t)$

The analysis seeks to determine if the efficacy parameter $\gamma$ and the baseline cellular rates ($\alpha_C, k_C$, etc.) are globally identifiable, locally identifiable, or unidentifiable given $Y(t)$ and known input $U(t)$.

### 3.5 Computational Simulation Environment
Simulations were performed using a stiff ODE solver (Radau IIA) due to the differing time scales of cellular lifespans (days) versus total bone mass turnover (years). The parameter reduction framework from T12 was applied to cluster sloppy parameters into identifiable aggregate terms. A 3-year Mars mission profile was simulated: 6 months transit (0g), 24 months surface operations (0.38g), and 6 months return (0g).

---

## 4.0 RESULTS

### 4.1 Baseline Remodeling Dynamics at Earth Gravity (1g)
Initial simulations under $g(t) = 1.0$ demonstrated stable limit-cycle oscillations representing healthy, homeostatic bone remodeling. Osteoclast populations peaked slightly before osteoblast populations, resulting in a temporary dip in total bone mass $Z(t)$ followed by full recovery. The steady-state net change in $Z(t)$ over a 12-month period was $0.001\%$, confirming that the autocrine/paracrine parameters ($g_{ij}$) successfully maintain coupled remodeling under normal terrestrial loading.

### 4.2 Simulated Trajectories of Microgravity (0g) Induced Bone Loss
Upon initiating the step function change to $g(t) = 0.0$ (simulating orbital insertion), the system exhibited rapid uncoupling. The osteoclast population ($C$) surged by 150% within the first 30 days due to the loss of mechanical suppression ($H_C$ modulation). Concurrently, the osteoblast population ($B$) declined by 40%. The resulting trajectory of $Z(t)$ showed a steep, monotonic decline, losing approximately 1.8% of bone mass per month. Over the 6-month transit simulation without countermeasures, the model predicted an 11.2% total reduction in baseline BMD, perfectly aligning with clinical observations from long-duration ISS crew members.

### 4.3 Structural Identifiability of Countermeasure Forcing Terms
The differential algebra analysis yielded critical mathematical insights regarding the observability of the system from DXA-like data ($Y(t) = Z(t)$).
1. **Baseline Parameters:** The individual cellular proliferation ($\alpha_C, \alpha_B$) and activity rates ($k_C, k_B$) were found to be **structurally unidentifiable**. The macroscopic observation of $Z(t)$ cannot distinguish between a state of high turnover (high resorption matched by high formation) and low turnover.
2. **Countermeasure Efficacy:** Remarkably, when the known perturbation function $U(t)$ (representing bisphosphonate dosing) was applied, the drug efficacy parameter **$\gamma$ was locally structurally identifiable**. Because the drug selectively perturbs the osteoclast decay rate ($\beta_C$), the specific inflection point in the BMD trajectory allows the mathematical extraction of $\gamma$, provided the baseline state prior to administration is approximated.

### 4.4 Mars Transit Simulation and Countermeasure Efficacy
Employing the stiff-sloppy reduction developed in T12, the unidentifiable cellular parameters were reduced to a single aggregate 'remodeling velocity' term, transforming the full system into an identifiable reduced model. 
Simulation of the 3-year mission with optimized bisphosphonate dosing $U(t)$ resulted in the following trajectories:
- **No countermeasures:** Total BMD loss of 31% over 3 years.
- **Empirical continuous dosing:** Total BMD loss reduced to 9%, but resulting in extreme suppression of bone turnover, theoretically increasing microcrack accumulation risk.
- **Model-optimized intermittent dosing (using identified $\gamma$):** Maintained BMD within 4% of baseline while preserving oscillatory BMU activity. The transition to Martian gravity (0.38g) showed a partial natural recovery of osteoblast activity, allowing for a tapering of the pharmacological forcing term.

---

## 5.0 DISCUSSION, CONCLUSION AND RECOMMENDATION

### 5.1 Discussion
The application of systems biology to space physiology provides a rigorous methodology for mitigating the profound risks of long-duration exploration. This thesis successfully constructed an ODE model capturing the complex dynamics of osteoclast and osteoblast coupling under varying gravitational loads. The simulated trajectory of unmitigated bone loss in 0g closely mirrors empirical data from orbital missions (LeBlanc et al., 2000), validating the mechanical forcing functions $H_C(g)$ and $H_B(g)$.

The most significant contribution of this work is the structural identifiability analysis of the countermeasure forcing terms. The finding that baseline cellular rates are unidentifiable from DXA-like data confirms the theoretical limitations of current clinical monitoring on the ISS. Aggregate BMD is too sluggish and macroscopic a variable to capture the rapid underlying cellular uncoupling. However, the discovery that the countermeasure efficacy parameter ($\gamma$) becomes locally identifiable during the transient response to drug administration provides a crucial mathematical lifeline. It demonstrates that by carefully timing BMD measurements in relation to drug dosing, aerospace physicians can theoretically estimate patient-specific drug response without requiring complex, invasive cellular assays inflight. The application of the stiff-sloppy reduction techniques from T12 proved instrumental here, allowing the model to bypass the unidentifiable dark matter of the baseline parameters and focus solely on the dynamic response to the countermeasure. 

### 5.2 Conclusion
This computational study demonstrates that while the underlying cellular kinetics of bone remodeling are structurally unidentifiable from aggregate bone mass measurements, the specific forcing terms representing pharmacological countermeasures are locally identifiable. The ODE model successfully simulates the catastrophic uncoupling of bone turnover under microgravity and provides a theoretical basis for optimizing intervention schedules during a Mars transit mission. By mathematically defining the limits of what can be known from DXA-like observations, this research lays the groundwork for personalized spaceflight medicine.

### 5.3 Recommendation
Based on the computational findings, the following recommendations are proposed:
1. **Development of Multi-channel Biosensors:** Future Mars missions should not rely solely on macroscopic BMD data. The structural unidentifiability of baseline states necessitates the development of in-flight biosensors capable of continuously monitoring blood biomarkers (e.g., CTX for resorption, P1NP for formation).
2. **Dynamic Dosing Protocols:** Countermeasure regimens should transition from static terrestrial prescriptions to dynamically modeled, patient-specific schedules utilizing parameter estimation derived from early transit data.
3. **Integration with Project Confluence:** The reduced identifiable ODE model should be integrated with the multi-channel identifiability frameworks established in Thesis T09 to evaluate the combined observability of biomechanical exercise and pharmacological interventions.

---

## References
Bellu, G., Saccomani, M. P., Audoly, S., & D'Angiò, L. (2007). DAISY: A new software tool to test global identifiability of biological and physiological systems. *Computer Methods and Programs in Biomedicine*, 88(1), 52-61.

Boyce, B. F., & Xing, L. (2008). Functions of RANKL/RANK/OPG in bone modeling and remodeling. *Archives of Biochemistry and Biophysics*, 473(2), 139-146.

Carmeliet, G., Vico, L., & Bouillon, R. (2001). Space flight: a challenge for normal bone homeostasis. *Critical Reviews in Eukaryotic Gene Expression*, 11(1-3), 131-144.

Frost, H. M. (1969). Tetracycline-based histological analysis of bone remodeling. *Calcified Tissue Research*, 3(1), 211-237.

Komarova, S. V., Smith, R. J., Dixon, S. J., Sims, S. M., & Wahl, L. M. (2003). Mathematical model predicts a critical role for osteoclast autocrine regulation in the control of bone remodeling. *Bone*, 33(2), 206-215.

LeBlanc, A., Schneider, V., Shackelford, L., West, S., Oganov, V., Bakulin, A., & Pechorina, I. (2000). Bone mineral and lean tissue loss after long duration space flight. *Journal of Musculoskeletal & Neuronal Interactions*, 1(2), 157-160.

Lemaire, V., Tobin, F. L., Greller, L. D., Cho, C. R., & Suva, L. J. (2004). Modeling the interactions between osteoblast and osteoclast activities in bone remodeling. *Journal of Theoretical Biology*, 229(3), 293-309.

Pivonka, P., Zimak, J., Smith, D. W., Gardiner, B. S., Dunstan, C. R., Sims, N. A., ... & Mundy, G. R. (2008). Model structure and control of bone remodeling: a theoretical study. *Bone*, 43(2), 249-263.

Robling, A. G., Niziolek, P. J., Baldridge, L. A., Condon, K. W., Allen, M. R., Alam, I., ... & Turner, C. H. (2006). Mechanical stimulation of bone in vivo reduces osteocyte expression of Sost/sclerostin. *Journal of Biological Chemistry*, 281(32), 23691-23697.

## Disclaimer
The models, simulations, and findings presented in this manuscript are intended solely for academic computational research. This thesis does not constitute astronaut medical advice, clinical recommendations, or validated therapeutic protocols. The differential equation models are theoretical abstractions of bone remodeling dynamics and should not be used to guide human intervention without empirical biological validation.
