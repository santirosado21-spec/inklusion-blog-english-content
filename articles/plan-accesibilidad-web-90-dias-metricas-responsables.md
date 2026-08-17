---
title: "Web Accessibility Plan in 90 Days: From Audit to Fixes That Actually Reach Production"
description: "A 90-day web accessibility plan: scope, audit, fixes, owners, and metrics to turn WCAG findings into continuous improvement."
datePublished: "2026-08-12"
sourceSlug: "plan-accesibilidad-web-90-dias-metricas-responsables"
sourceUrl: "https://inklusion-blog.vercel.app/blog/plan-accesibilidad-web-90-dias-metricas-responsables/"
language: "en"
---

# Web Accessibility Plan in 90 Days: From Audit to Fixes That Actually Reach Production

**Direct answer:** a 90-day web accessibility plan must delimit critical user journeys, establish a technical and user-based baseline, prioritize barriers by impact, assign owners, fix reusable components, and verify every change before it reaches production. Its realistic goal is to reduce blockers and put permanent controls in place — not to promise that a complex site will be "100% accessible" on a calendar schedule.

The audit usually arrives as a file full of numbered findings. The problem starts when nobody knows which ones are blocking a purchase, who modifies the shared component, or what evidence is needed to close the ticket. Three months later, the report is still pristine. The product, not so much.

> An audit without an owner or a closure criterion describes the debt. It does not reduce it.

## What must be decided before the 90 days begin?

Define scope by tasks, not merely by number of pages. Registration, search, purchase, payment, document access, support, and account recovery usually matter more than a randomly chosen sample of URLs. The W3C explains that the [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) provide verifiable criteria for making content perceivable, operable, understandable, and robust.

Choose a reference version of WCAG and a target conformance level based on obligations, risks, and context. Document the browsers, devices, and assistive technologies that will be part of testing. If the product depends on third parties — a payment engine, chat, scheduling tool, or authentication service — include them in the map even if you cannot fix their code directly.

**Fact:** an automated test does not evaluate every criterion, nor does it demonstrate that a task can be completed. **Operational decision:** combine automation, manual review, keyboard testing, assistive technologies, and testing with people when risk and scope require it.

## Days 1 to 15: how do you build a useful baseline?

### Map journeys, components, and owners

Link each critical task to its templates and components: header, menu, form, modal, table, media player, or date picker. Add the product, design, development, content, and vendor owners. When the same component fails on 40 pages, the plan must show a system-level fix, not 40 patches.

### Record barriers with reproducible evidence

Each finding needs a location, steps to reproduce, observed result, expected result, people potentially affected, the related criterion, and evidence. A short screen recording, a screenshot, and a code snippet can speed up diagnosis, but they do not replace a clear explanation.

### Establish the starting point

Measure how many essential tasks can be completed with the keyboard and selected assistive technologies; how many critical blockers exist; what percentage of shared components has been reviewed; and how long it takes the team to assign a finding. Our [web accessibility audit guide](https://inklusion-blog.vercel.app/blog/auditoria-accesibilidad-web-wcag-checklist-mexico/) details a structure for evaluating and prioritizing without reducing the review to a scan.

## Days 16 to 35: how do you prioritize without making everything "urgent"?

Use at least four variables: severity for the person, frequency of the journey, scope of the component, and technical dependency. A button with no accessible name that prevents payment deserves more attention than an out-of-order heading on a secondary page, even though both must be fixed.

- **Blocker:** prevents completing an essential task with no equivalent alternative.
- **High:** requires disproportionate effort, causes serious errors, or affects critical content.
- **Medium:** makes comprehension or operation difficult, but a usable path exists.
- **Low:** has limited impact and does not block the task, while still constituting debt.

Then look for multipliers. Fixing the shared modal, form, or heading system can resolve dozens of instances at once. Priority should not be decided solely by lowest cost: "we fixed 200 decorative alt texts" sounds productive, but it does not compensate for a payment flow that is impossible to complete with a keyboard.

## Days 36 to 65: how do you get fixes into production?

### Turn findings into acceptance criteria

Avoid tickets like "make the form accessible." Specify verifiable behaviors: every field has a programmatic name; the error message identifies the field and explains how to resolve it; focus moves predictably; the session allows time to be extended; and submission works with a keyboard and screen reader in the agreed configurations.

### Fix at the design-system level

When the barrier lives in a reusable component, modify its source, documentation, and tests. Tag the corrected version and retire obsolete patterns. That way the team stops reintroducing the same problem every time a new screen is created.

### Test on a branch, then test the complete journey

A local fix can break another state. Test empty, error, loading, success, expired session, and real content. Then verify the full task. If the field now has a label but the verification code expires before it can be entered, the barrier persists with better HTML.

To organize a representative sample and verify complete processes, see our analysis of [WCAG-EM 2 and digital product evaluation](https://inklusion-blog.vercel.app/blog/wcag-em-2-evaluacion-accesibilidad-productos-digitales-2026/).

## Days 66 to 80: when should you include testing with people with disabilities?

User testing is especially valuable in complex journeys, high-impact decisions, and experiences where technical conformance does not reveal cognitive load, trust, or autonomy. Do not use it to replace basic technical controls or to ask a person to find all the errors.

Define tasks, accommodations, consent, compensation, data protection, and how observations will be recorded. Distinguish the observed barrier from individual preference and avoid generalizing. The [guide to accessibility testing with people with disabilities](https://inklusion-blog.vercel.app/blog/pruebas-accesibilidad-con-usuarios-discapacidad-guia/) proposes a process for turning sessions into decisions without using participants as a certification mechanism.

## Days 81 to 90: how do you close the cycle without declaring victory too soon?

Repeat the tasks and tests from the baseline. A ticket closes only when evidence of the agreed criterion exists and the fix is in the environment that people will actually use. If a blocker remains, document a temporary alternative, an owner, a date, and the risk — do not hide it inside an overall percentage.

Publish a next-steps roadmap: pending components, legacy content, vendors, training, and regression frequency. A 90-day plan should end with accessibility integrated into weekly work, not with a folder titled "phase two" that nobody ever opens again.

## What metrics show real progress?

Avoid a single score. Automated percentages can serve as a regression signal within the same scope and tool, but they do not represent the full experience and are not equivalent to conformance.

- **Outcome:** percentage of essential tasks completable in the test configurations.
- **Risk:** open critical blockers, their age, and recurrence rate.
- **Velocity:** time from detection to assignment, fix, and verification.
- **Coverage:** components, templates, states, and journeys evaluated.
- **Prevention:** acceptance criteria incorporated and regressions stopped before production.
- **Experience:** barriers observed with users, supports required, and task autonomy.

**Hypothesis:** fixing shared components first and adding regression tests will reduce recurrence during the following quarter. Verify this by comparing new findings per component and the proportion caught before launch.

## Five mistakes that cause a roadmap to fail

1. **Measuring pages and forgetting tasks.** A correct homepage does not compensate for a blocked payment flow.
2. **Assigning everything to development.** Design, content, procurement, and product also create or prevent barriers.
3. **Fixing instances instead of components.** The same error comes back under a different name.
4. **Closing tickets on code change alone.** Without retesting there is no evidence of resolution.
5. **Promising "100% accessible."** Content, dependencies, and the product change; management must continue.

## Frequently asked questions

### What does a web accessibility plan include?

Scope, baseline, priorities, owners, fixes, testing, training, vendors, and metrics.

### Can a site be made accessible in 90 days?

It can reduce critical barriers and put controls in place; full conformance depends on scope and must be verified.

### What gets fixed first?

Blockers on essential tasks, shared components, and high-impact or high-risk issues.

### What metrics are appropriate?

Completable tasks, blockers, recurrence, time to fix, coverage, and evidence from user testing.

### Does an automated tool demonstrate conformance?

No. It must be combined with manual review and interaction testing with assistive technologies.

## Turn Accessibility Findings into a Verifiable Plan

Inklusion helps organizations evaluate digital barriers, prioritize fixes, and build a continuous-improvement practice.

[Learn about Inklusion's web accessibility solutions](https://www.inklusion.com.mx/accesibilidad-web/)
