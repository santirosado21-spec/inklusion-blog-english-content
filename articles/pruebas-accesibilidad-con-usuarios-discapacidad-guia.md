---
title: "Accessibility Testing with People with Disabilities: How to Learn Without Turning the Session into an Exam"
description: "How to plan accessibility testing with people with disabilities: objectives, recruitment, adjustments, sessions, findings, and metrics."
datePublished: "2026-08-10"
sourceSlug: "pruebas-accesibilidad-con-usuarios-discapacidad-guia"
sourceUrl: "https://inklusion-blog.vercel.app/blog/pruebas-accesibilidad-con-usuarios-discapacidad-guia/"
language: "en"
---

# Accessibility Testing with People with Disabilities: How to Learn Without Turning the Session into an Exam

**Direct answer:** an accessibility test with users observes how people with disabilities complete real tasks using their own technologies and strategies. To do it well, the organization must define objectives, recruit relevant profiles, ask about adjustments, compensate participation, prepare accessible materials, and document barriers without evaluating the person. These sessions complement a WCAG review; they do not replace it.

There is an enormous difference between knowing that a button "has a label" and discovering that the label does not allow a user to distinguish "save draft" from "submit request." The first answer comes from a technical check. The second appears when someone tries to finish the work.

> In an accessibility test, a block is not an error on the part of the participant. It is evidence about the product.

## What are accessibility tests with users for?

The W3C explains in its guide on [involving users in accessibility evaluation](https://www.w3.org/WAI/test-evaluate/involving-users/) that involving people with disabilities helps to understand how they use the web, assistive technologies, and their adaptive strategies. It can also uncover accessibility and usability problems more effectively.

A well-designed session can show, for example, that:

- the focus order allows forward navigation, but forces the user to move through dozens of controls before reaching the main action;
- the error message is announced, yet does not explain how to correct the data;
- the video call has captions, but the link to request an adjustment does not work with a keyboard;
- a flow is technically operable and yet imposes an unnecessary cognitive load.

The test connects the finding to a consequence: abandonment, dependence on another person, exposure of information, additional time, or inability to complete the task.

## Why don't they replace a WCAG audit?

The W3C is clear: evaluation with users cannot on its own cover all types of disability, strategies, and assistive technologies. Nor does it automatically determine conformance with a standard. It must be combined with WCAG-based evaluation.

The reverse also matters. A technical audit can identify non-conformances, but does not always explain which one interrupts the journey first, or how several minor friction points accumulate. The W3C guide on [combined expertise in evaluation](https://www.w3.org/WAI/test-evaluate/combined-expertise/) notes that an effective review requires knowledge of technology, tools, barriers, assistive technologies, and guidelines.

Our position is straightforward: WCAG provides criteria; people contribute situated experience. Presenting them as competing options impoverishes the decision.

## How do you prepare a test plan?

### 1. Choose decisions, not a demonstration

The objective should not be "to see whether the site is accessible." It is better to frame a concrete decision: finding out whether a person can request a quote, complete a job application, recover their password, or find support without external help.

Select between three and five critical tasks. Describe the outcome, not the clicks. "Find and purchase the right plan" allows strategies to be observed; "click on Pricing and then on Buy" rehearses the team's script.

### 2. Define relevant profiles

Disability is not a single variable. The plan must consider the task, the context of use, digital experience, and the relevant technologies or strategies: screen reader, magnification, keyboard navigation, voice recognition, captions, easy-read, or others.

There is no universal number of participants that represents all disability. A small round can reveal significant blocks, but its results must be reported with explicit limits. "Three people did not find the control" is evidence; "people with disabilities cannot use it" is a generalization the sample does not support.

### 3. Ask about adjustments before the session

The invitation must be in an accessible format and state the purpose, duration, modality, data use, and compensation. Include an open question: "What do you need to participate on equal terms?" Do not require disclosure of a diagnosis if knowing the adjustment is sufficient.

### 4. Compensate time and experience

As an Inklusion practice, we recommend offering clear and equivalent compensation to participants who fulfill the same role. Lived experience contributes professional value. Treating it as implicit volunteering transfers the cost of the research to those who already face the barrier.

## How do you conduct a session without evaluating the person?

Before starting, confirm consent, recording, breaks, and preferred form of communication. Allow the person to use their own equipment and usual configuration when the objective is to observe a real experience. If the test requires a controlled device, explain why and verify that the configuration is compatible.

During the task, ask the person to share what they are trying to do, without requiring constant narration if it interferes with their technology or concentration. The moderator may ask "what did you expect to find?" or "what information is missing?", but should avoid showing the way too soon.

If a block appears, record:

- the task and the exact point;
- what the person expected;
- what technology or strategy they were using;
- whether they were able to recover and with what support;
- the consequence: delay, error, abandonment, dependence, or risk;
- the available evidence, taking care with personal data.

Stop a task when continuing would cause unnecessary frustration, expose information, or no longer generate learning. The objective is to study the product, not to measure endurance.

## How do you turn observations into changes?

A two-hour video is not a backlog. Each finding needs a reproducible description, evidence, affected users, consequence, proposed severity, and an owner. Link it to the WCAG criterion where a relationship exists, without forcing a criterion onto every usability problem.

A useful prioritization combines four questions:

- **Impact:** does it prevent or hinder an essential task?
- **Scope:** in how many journeys, templates, or channels does it appear?
- **Frequency:** how regularly is the task performed?
- **Risk of recurrence:** will the component or process reintroduce the barrier?

After correcting, retest the journey. Closing a ticket because the code changed demonstrates activity; verifying that the person can complete the task demonstrates progress.

## What metrics help without reducing the experience to an average?

Record task completion, blocks, support requested, indicative time, severity, and recurrence. Segment results by task and configuration where relevant; an overall average can hide the fact that one group never completed the task.

It is also worth measuring the internal process: percentage of critical findings corrected, time to validation, recurrence by component, and proportion of priority journeys retested.

Time requires context. An experienced screen reader user may complete a task faster than a person without a disability; another person may take longer due to unfamiliarity with the product. The useful data point is not who "won," but where the design imposed avoidable steps, doubts, or dependencies.

## Five errors that invalidate the learning

1. **Inviting one person and asking them to represent everyone.** Document the profile and limit the conclusion.
2. **Testing only the home page.** Prioritize complete processes and error states.
3. **Arriving with an inaccessible prototype of the session itself.** Review the invitation, consent, platform, materials, and support channel.
4. **Correcting the participant.** If the moderator explains the control, first record that the product did not explain it.
5. **Storing findings without an owner.** Define a date, owner, acceptance criteria, and subsequent validation.

To structure the technical scope and sample, see the analysis of [WCAG-EM 2 for digital products](https://inklusion-blog.vercel.app/blog/wcag-em-2-evaluacion-accesibilidad-productos-digitales-2026/). To order corrections by severity and evidence, review our [web accessibility audit guide](https://inklusion-blog.vercel.app/blog/auditoria-accesibilidad-web-wcag-checklist-mexico/).

## Frequently asked questions

### What is accessibility testing with users?

Sessions where people with disabilities attempt real tasks and reveal barriers, strategies, and consequences in the product.

### Do they replace a WCAG audit?

No. User experience and technical evaluation answer different questions and must be combined.

### How many people should participate?

It depends on tasks, profiles, technologies, and risks. A small sample can uncover barriers, but does not represent all people.

### Should participation be paid?

Inklusion recommends compensating time and experience with clear and equivalent criteria.

### What should be measured?

Completion, blocks, support, time with context, severity, recurrence, and consequences for the person and the business.

## Include real experience in your accessibility evaluation

Inklusion supports organizations that need to identify barriers, listen to people, and turn evidence into concrete improvements.

[Learn about the inclusion consultancy](https://www.inklusion.com.mx/consultoria-en-inclusion/)
