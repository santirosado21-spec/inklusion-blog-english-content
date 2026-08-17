---
title: "How to Buy Accessible Software: An Evaluation Checklist for Organizations"
description: "Checklist for evaluating and purchasing accessible software: requirements, ACR/VPAT, demonstrations, acceptance testing, contract terms, metrics, and follow-up."
datePublished: "2026-08-07"
sourceSlug: "comprar-software-accesible-checklist-proveedores"
sourceUrl: "https://inklusion-blog.vercel.app/blog/comprar-software-accesible-checklist-proveedores/"
language: "en"
---

# How to Buy Accessible Software: An Evaluation Checklist for Organizations

**Direct answer:** to buy accessible software, first define the tasks and requirements the product must support; then request an Accessibility Conformance Report (ACR), review its gaps, require an accessible demonstration, and test critical workflows using a keyboard and assistive technologies. The decision should conclude with a contract that includes acceptance criteria, responsible parties, correction timelines, and rules for future updates.

Buying accessibility at the end almost always means buying twice: first the license, then the remediation, the workaround, or the migration. The solution is not to ask for a more polished promise. It is to change the way you evaluate.

> A vendor does not demonstrate accessibility by saying "we comply with WCAG." They demonstrate it by explaining which version they evaluated, against which criteria, using which method, what failed, and when they will fix it.

## What does "accessible software" mean in a procurement context?

Accessible software enables people with various disabilities to complete relevant tasks independently and safely. The review may cover a web or mobile application, desktop software, a learning platform, a human resources system, a CRM, a kiosk, documentation, support, and integrations.

The key word is **tasks**. An accessible login does not compensate for a performance review that cannot be submitted using a keyboard. A flawless public-facing page does not resolve an administrative console that is inaccessible to an employee.

That is why the scope must be written down before opening the commercial comparison. In a talent platform, for example, critical use cases might include posting a vacancy, requesting adjustments, applying, scheduling an interview, evaluating, signing documents, and completing onboarding.

## What requirements should be defined before requesting proposals?

Start with a short brief that connects business needs and accessibility:

- **Users:** candidates, employees, customers, administrators, and support staff.
- **Critical workflows:** the tasks that cannot fail or depend on informal assistance.
- **Platforms:** web, iOS, Android, desktop, kiosk, and generated documents.
- **Assistive technologies:** keyboard navigation, screen reader, magnification, voice recognition, captions, and others as relevant.
- **Standard:** WCAG version and level, plus any requirements applicable to the market or contract.
- **Third-party content:** payments, signatures, maps, video calls, assessments, and integrations.
- **Evidence:** ACR, testing methodology, known issues, and roadmap.
- **Acceptance:** who tests, what outcome is expected, and what happens if barriers are found.

The [Section508.gov guide for buying accessible products and services](https://www.section508.gov/buy/) organizes procurement into six steps: define requirements, conduct market research, develop solicitation language, request accessibility information, evaluate proposals, and validate contractor compliance. Although that guide responds to the U.S. federal context, the sequence is a useful operational reference for any procurement team.

## What are a VPAT and an ACR?

The [Information Technology Industry Council (ITI)](https://www.itic.org/policy/accessibility/vpat) publishes the Voluntary Product Accessibility Template, known as the VPAT. It is a template for documenting how a product or service addresses accessibility criteria. When completed with results, the document is called an **Accessibility Conformance Report (ACR)**.

Version 2.5Rev from ITI, published in April 2025, provides four states per criterion: "supports," "partially supports," "does not support," and "not applicable," along with explanations. Editions also exist oriented toward Section 508, the European Union, WCAG, and international requirements.

One distinction prevents many mistakes: **VPAT is the template; ACR is the completed report**. In commercial conversations people say "send me your VPAT," but the buyer needs the filled-in, current document corresponding to the product being evaluated.

It is also not a certificate issued by ITI. It typically contains statements from the manufacturer or vendor. It serves to research and ask questions; it does not replace validation.

## How do you review an ACR without getting lost in the document?

### 1. Confirm product, version, and date

A report from three years ago may describe an interface that no longer exists. Verify the name, edition, modules, platforms, and evaluation date. If the product is updated every week, ask how the evidence is kept current.

### 2. Check the correct standard

WCAG 2.0, 2.1, and 2.2 are not interchangeable. The conformance level and the VPAT edition also matter. Choose according to your requirements and avoid accepting a document whose framework does not correspond to the procurement.

### 3. Read the gaps first

Look for "partially supports" and "does not support." The explanation should indicate where the problem occurs, who it affects, and whether a temporary workaround exists. "Will be fixed in a future version" without a number or date is a wish, not a plan.

### 4. Detect vague responses

Identical phrases across dozens of criteria, absence of methods, "not applicable" without justification, or absolute claims all warrant questions. A credible report acknowledges limitations and provides evidence.

### 5. Map each finding to a task

Not all defects carry the same consequence. An incorrect focus order in the payment workflow can block a sale; an incomplete label in a rarely used section may be minor. Priority comes from severity, frequency, and task—not from the raw number of criteria.

## What should the vendor demonstrate?

Send the scripts before the demonstration and ask the vendor to execute the critical workflows live. A useful demo includes:

- navigating the product using only a keyboard and showing a visible focus indicator;
- using a screen reader with at least one agreed-upon browser and technology combination;
- increasing text size or zoom without losing content or functionality;
- activating captions and reviewing multimedia controls where applicable;
- triggering form errors and verifying that they are identified and explained;
- showing documents, emails, and reports generated by the system;
- navigating the administrative interface, not only the public-facing experience;
- demonstrating how to request support for an accessibility barrier.

The demonstration should not be designed to "catch" the vendor. It should allow both parties to understand the reality before the contract is signed. A finding that is acknowledged, scoped, and has a verifiable correction may be more manageable than a promise of perfection without evidence.

## How do you conduct an acceptance test?

Combine four layers:

1. **Automated review:** detects patterns such as missing accessible names, contrast issues, or structure problems. It does not certify full conformance.
2. **Manual testing:** keyboard, focus, zoom, reflow, forms, messages, multimedia, and components.
3. **Assistive technologies:** use defined combinations and record steps, expected result, and actual result.
4. **Participation of people with disabilities:** incorporate lived experience to detect friction that a technical checklist does not explain.

For evaluations of complete sites, the [WCAG-EM methodology from W3C/WAI](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) offers a structure for defining scope, exploring the site, selecting a sample, and auditing it. In a procurement context it can be adapted to the modules and workflows that make up the product.

Keep reproducible evidence: version, environment, steps, screenshots or video where appropriate, related criterion, severity, responsible party, and retest date. The [web accessibility audit guide](https://inklusion-blog.vercel.app/blog/auditoria-accesibilidad-web-wcag-checklist-mexico/) explains how to organize findings and corrections.

## How do you compare vendors using a useful matrix?

Do not turn the decision into "who has the fewest red cells." Weight each criterion according to the service:

- **40% — critical workflows:** can people complete the essential tasks?
- **20% — evidence:** is the ACR current, specific, and does it explain methods?
- **15% — remediation:** are there responsible parties, committed dates, and versions?
- **10% — product governance:** do they test each release and train their teams?
- **10% — support:** is there an accessible channel and defined response times?
- **5% — documentation:** are manuals, training materials, and other resources also accessible?

The weights are an example, not a universal standard. A clinical platform or an emergency system may require different tolerances and weightings. Document why you assigned each weight; that makes the decision explainable.

## What must be written into the contract?

- product, modules, platforms, and content included;
- agreed standard, version, and conformance level;
- current ACR and evaluation methodology;
- workflows and acceptance criteria before go-live;
- list of known gaps, temporary workarounds, and correction dates;
- timelines by severity and an escalation mechanism;
- obligation to maintain accessibility in updates;
- advance notice when a change affects assistive technologies;
- reasonable access to test environments;
- accessibility of support, documentation, and training;
- responsibility for integrations and subcontractors;
- contractual remedies if agreed criteria are not met.

The final wording requires legal review. The operational objective is to prevent "accessible" from remaining a decorative adjective with no deliverable, no test, and no consequence.

## What should you measure after purchasing?

Accessibility can degrade with an update, a new integration, or poorly published content. Review:

- percentage of critical workflows tested in each relevant release;
- open defects by severity and age;
- time from report to verified resolution;
- recurrence of previously corrected barriers;
- currency of the ACR;
- user incidents and requests;
- vendor compliance with committed dates;
- participation of people with disabilities in periodic testing.

A low number of reports does not prove that the product is accessible. It may also mean that the channel is unknown, is not accessible, or that no one expects a response anymore. Combine metrics with scheduled testing and conversation.

## Brief checklist before signing

- ☐ We defined users, platforms, and critical tasks.
- ☐ We specified the standard, version, and level.
- ☐ We received a current ACR for the exact product.
- ☐ We reviewed partially supported, not supported, and not applicable criteria.
- ☐ The vendor demonstrated workflows using a keyboard and assistive technology.
- ☐ We tested both the public-facing and administrative experiences.
- ☐ We documented barriers, severity, and workarounds.
- ☐ We agreed on corrections with a responsible party, date, and version.
- ☐ The contract includes acceptance criteria and accessibility requirements for updates.
- ☐ An accessible support and escalation channel exists.
- ☐ We defined metrics and a post-purchase review process.

## Frequently asked questions

### What is accessible software?

It is a product that enables people with various disabilities to complete their relevant tasks. The evaluation includes the interface, content, documentation, support, and integrations.

### What is the difference between a VPAT and an ACR?

VPAT is the ITI template. When it is completed with evaluation results it becomes an Accessibility Conformance Report, or ACR.

### Is an ACR enough to approve a purchase?

No. You must review its scope and currency, demonstrate critical workflows, conduct testing, and convert gaps and corrections into contractual commitments.

### What should the contract include?

Standard, scope, evidence, acceptance tests, correction timelines, support, updates, responsible parties, and consequences for non-compliance.

### How do you compare two vendors that both have failures?

With a matrix that weights severity, affected tasks, users, frequency, workarounds, evidence, and the real capacity to correct and sustain accessibility.

## Evaluate accessibility before committing to a purchase

Inklusion supports organizations that need to identify digital barriers, prioritize risks, and turn accessibility into concrete decisions.

[Learn about the inclusion consulting service](https://www.inklusion.com.mx/consultoria-en-inclusion/)
