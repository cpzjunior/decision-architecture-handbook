# 1. Foundations of Decision Architecture

This guide proposes six foundations for understanding decisions. They do not constitute a universal definition of Decision Architecture, nor should they be understood as stages of a process or as a list of mandatory elements. They are a conceptual proposition intended to make recurring characteristics of decisions and the relationships between them explicit.

A foundation, in this context, is a structural characteristic of a decision. It helps us understand a dimension that is present when a choice is considered, made, and produces effects. It does not, by itself, define how the decision should be conducted. Its function is to provide a reference for understanding the situation before determining how to act upon it.

This distinction is important because concrete decisions are often addressed through methods, techniques, and frameworks developed for specific contexts. These approaches organize ways of working and provide mechanisms for dealing with specific problems. The foundations proposed here are at a prior level: they seek to describe characteristics of the decision itself, regardless of the particular way used to conduct it.

The characteristics of a decision, however, do not appear in isolation. A decision takes place within some domain and starts from certain conditions. It is guided by objectives, but these objectives need to be considered in light of what we do not yet know. The choice produces consequences, and those consequences modify the conditions under which subsequent decisions will be made.

This structure can be observed in different types of decisions. An architectural decision, a business decision, a project decision, or a personal decision have distinct natures, but all of them occur in some situation, pursue some outcome, are made with incomplete knowledge, and produce effects that may alter what will be possible to do later.

The objective of this chapter is not to introduce new terminology to replace already established concepts. Many of the ideas presented here are well known and appear, under different names and levels of formalization, in disciplines such as architecture, management, engineering, entrepreneurship, and product development.

The proposition is different: to start from the most basic questions we need to answer in order to understand a decision and, from them, identify the needs that derive from them. Instead of starting with the available methods and trying to fit the decision into their structures, we begin by asking what needs to be understood about the decision itself.

What are the minimum conditions we need to know in order to understand a decision? What defines the field in which it takes place? From what situation is it made? What guides the choice? What do we still not know? What changes as a consequence of the decision? And how do these changes constrain subsequent decisions?

It is from these questions that we arrive at the foundations presented below. Each seeks to answer a more basic question about the structure of the decision and, from it, makes it possible to derive needs that can be addressed through different practices and approaches.

## 1.1. Every decision occurs within one or more domains

Every decision occurs within one or more domains of knowledge, activity, or problem. The domain establishes the field in which the decision is understood and provides concepts, knowledge, criteria, and practices used to interpret situations and evaluate alternatives.

A decision about a payments platform, for example, may require knowledge of architecture, security, finance, product, operations, and regulation. Each domain contributes its own references for understanding different aspects of the decision.

The participation of different domains does not simply mean bringing experts together in the same discussion. Each domain may see a different part of the situation and use different criteria to evaluate the alternatives. A technically suitable alternative may be financially unfeasible. A financially attractive solution may create operational risks. A decision suitable for the product may conflict with a regulatory constraint.

Therefore, the domain is not merely the subject we are talking about. It influences what we consider relevant, which concepts we use, and which questions need to be asked.

A software architecture decision mobilizes concepts such as components, interfaces, technologies, quality attributes, and dependencies. A project management decision may involve scope, schedule, budget, resources, risks, and dependencies. An entrepreneurial decision may involve customers, market, value proposition, business model, and resource allocation.

Specialized knowledge provides references for analysis, but it does not determine a single answer. Two decisions may occur in the same domain and arrive at different choices because they have different objectives, conditions, constraints, or alternatives.

This also explains why practices developed in one domain should not be automatically transferred to another. A practice may make sense because it responds to a specific need in that field and because its concepts, criteria, and artifacts were built for particular conditions.

The first need produced by this foundation is domain delimitation. We need to know which fields the decision belongs to, which knowledge is relevant, which participants need to be considered, and which boundaries define what is being analyzed.

Delimiting does not necessarily mean choosing a single domain. A decision may deliberately cross boundaries between areas. The objective is to make these boundaries visible so that we can understand which perspectives are part of the decision and which knowledge we need to mobilize.

This need can be addressed through practices such as scope definition, boundary identification, domain modeling, stakeholder identification, and the creation of a common language. Different frameworks organize these practices in different ways, but all are, to some extent, responding to the need to understand where the decision is situated.

## 1.2. Every decision starts from an initial context

Every decision starts from an existing situation. The initial context brings together the relevant conditions for understanding the decision at the moment it is considered.

Domain and context are not the same thing. The domain defines the field in which the decision makes sense and provides the references used to understand it. The context defines the particular conditions in which it occurs.

These conditions may include available resources, constraints, information, evidence, assumptions, commitments, dependencies, previous decisions, and other circumstances that influence the possibilities being considered.

The same domain may present completely different contexts. An architecture decision may occur in a new system or in a legacy environment. There may be an experienced team or a team that still needs to acquire knowledge. There may be an available budget or a significant financial constraint. There may be technological freedom or a contractual dependency that limits the alternatives.

These differences are not peripheral details. They can completely change the set of viable alternatives and how each alternative should be evaluated.

Context is also not static. New information may emerge, resources may be consumed, constraints may change, and previous decisions may produce unexpected effects. Therefore, the context considered at the beginning of a decision may not be exactly the same context encountered during its execution.

This characteristic also explains why previous experience cannot be treated as a ready-made solution. Past experience may provide useful references, patterns, and hypotheses, but its applicability depends on current conditions.

Experience provides references. Context determines their applicability.

The second need produced by this foundation is the explicit definition of the decision's conditions. We need to identify what exists, which resources are available, which constraints must be respected, which assumptions are being made, which dependencies exist, and which information is not yet available.

This need is addressed by practices involving diagnosis, constraint gathering, assumption identification, dependency analysis, understanding the existing environment, and identifying current conditions. The objective is not to describe all of reality, but to make visible the conditions that actually influence the decision.

This is particularly important when a method or framework will be applied. The practices of a framework were developed to address certain needs and assume certain conditions of application. Using them without verifying whether these conditions exist can produce a situation in which we correctly follow the method but address a problem different from the one we actually have.

This is where one of the differences between knowing a method and knowing how to use it appears. The proper application of a practice depends on the ability to recognize the conditions for which it was designed and verify whether those conditions are present in the current situation.

## 1.3. Every decision is guided by one or more objectives

Every decision is related to one or more outcomes that are intended to be achieved, preserved, or avoided. These objectives guide, explicitly or implicitly, the evaluation of alternatives and provide a reference for determining what is expected to be obtained.

An objective may be clearly formulated or remain implicit. A person may decide to reduce costs without having previously defined how much they intend to reduce or within what timeframe. An organization may decide to modernize a system without clarifying whether the primary objective is to reduce costs, increase capacity, decrease risks, or enable a new business strategy.

The existence of an implicit objective does not necessarily mean that the decision is invalid. It means that part of the logic guiding the choice has not yet been made explicit.

Making objectives explicit also makes it possible to compare alternatives. Without knowing what we are trying to achieve, we may compare solutions based on preferences, familiarity, or circumstantial criteria that do not represent what actually matters.

Objectives may also conflict. Reducing costs may conflict with increasing quality. Accelerating delivery may increase risks. Preserving an existing architecture may limit future changes. Increasing flexibility may raise complexity.

Therefore, defining objectives does not simply mean producing a list. It is necessary to understand the relationships between them and recognize when an alternative meets one objective well but produces unfavorable consequences for another.

Objectives may also change during the analysis. New information may show that what initially seemed important is no longer relevant, that an objective is unfeasible under the existing conditions, or that there is a more important outcome that had not been considered.

This creates an important relationship between objective and problem. A situation becomes a problem in relation to some intended outcome. If the objective changes, the interpretation of the situation may also change.

For example, “replace the current system” may initially appear to be a technical problem. But if the actual objective is to reduce the time required to launch new products, then replacing the entire system may not be the only alternative. The problem may be related to a specific capability rather than to the technology as a whole.

In this sense, problem and objective should not be treated as completely independent elements. The definition of what needs to be solved depends, in part, on the outcome we consider necessary to achieve.

The third need produced by this foundation is the definition of evaluation criteria. If there are objectives, we need references that allow us to evaluate alternatives and later verify whether the outcome achieved meets what was intended.

These criteria may take different forms. They may be requirements, metrics, indicators, quality attributes, success conditions, acceptable limits, or other references appropriate to the domain and objective. Not every objective needs to be reduced to a metric. What matters is having a sufficiently clear way to evaluate the relationship between the choice and what is intended to be achieved.

## 1.4. Every decision involves some degree of uncertainty

A decision involves choosing between possibilities without completely knowing their consequences or future conditions. The degree of uncertainty varies according to the quantity and quality of available information, accumulated experience, and the predictability of the situation.

Some decisions have a large amount of data and evidence available. Others must be made with scarce information and many unknowns. There are also situations in which the consequences of an alternative are largely known. In such cases, uncertainty may be small, but there is still a choice about how to act.

Uncertainty may also have different origins. We may not sufficiently understand the problem, not know how a solution will work, be unable to predict the behavior of users or customers, depend on external factors, or not know how certain variables will evolve.

This distinction is important because different types of uncertainty require different forms of investigation. When we do not understand the problem, we need to learn about the situation. When we do not know whether a solution works, we may need to experiment. When we know the alternatives but do not know which consequences will occur, we may need to analyze risks and scenarios.

Uncertainty does not need to be eliminated before acting. We can seek information, consult experts, test hypotheses, conduct experiments, build prototypes, or wait for new data.

Each alternative, however, has its own cost. Further investigation may reduce what is unknown, but it may also consume time, resources, or opportunities. An experiment may generate evidence, but it requires investment. Waiting for more information may improve a decision or simply delay a necessary action.

Deciding therefore involves evaluating not only which alternatives are available, but also how much it is worth learning before acting.

This evaluation also depends on the nature of the consequences. When a decision is easily reversible, it may be acceptable to proceed with a higher degree of uncertainty. When a choice creates commitments that are difficult to undo, the cost of a premature decision may be much greater.

The fourth need produced by this foundation is the treatment of the unknown. We need to identify what we still do not know, assess its importance, and decide how to deal with this uncertainty.

Hypotheses, evidence, experiments, prototypes, research, scenarios, risks, and opportunities are different ways of dealing with what we do not yet know.

Lean Startup, for example, structures practices for turning hypotheses into experiments and learning. Design Thinking uses investigation, prototyping, and testing activities to learn about needs and possible solutions. Risk management structures the identification and analysis of uncertain events and their possible consequences.

These approaches are not equivalent and should not be applied merely because a decision contains uncertainty. The issue is to understand what uncertainty exists, what knowledge is missing, and which practice can produce relevant evidence for the decision.

## 1.5. Every decision produces direct and indirect consequences

A decision produces more than an immediate outcome. It can commit resources, create dependencies, establish constraints, eliminate paths, or make certain changes more costly. Some of these consequences appear directly after the decision, while others emerge as indirect effects of what was changed.

Consequences can also propagate to other parts of the situation. A decision about technology can alter a team's work. A project decision can modify responsibilities, schedules, or resources. A product decision can affect customers, users, or partners. An organizational change can create new commitments for other areas.

When a decision produces effects on other people or groups, a need for communication also arises. It is necessary to make clear what was decided, why the decision was made, what consequences are expected, and what changes for those who will be affected or need to act as a result of it. In this sense, communication is not merely an activity that follows the decision, but part of dealing with its consequences.

A decision can also preserve options, generate new alternatives, or produce information useful for subsequent decisions. Its effects, therefore, are not limited to what happens immediately after the choice. Some consequences modify the conditions under which other decisions will be made.

This is how we can understand the space of possibilities. It represents what can be done from a given point in time, considering the existing resources, commitments, dependencies, and constraints. The consequences of a decision can alter this space, making some possibilities more accessible, others more difficult, and some infeasible.

Changing the space of possibilities does not necessarily mean reducing options. A choice can eliminate certain paths while simultaneously creating others. A new technological capability can open alternatives that did not exist. A commercial decision can create access to one market and close another.

Every choice also involves trade-offs. By favoring a particular outcome, a decision may require concessions in other objectives, criteria, or possibilities.

Improving performance may increase cost. Reducing time may increase risk. Increasing flexibility may raise complexity. Preserving compatibility may limit the ability to evolve. In many cases, there is no alternative that simultaneously maximizes all objectives.

This dynamic can be observed through the idea of optionality. Some choices preserve a greater capacity for future change. Others increase commitments and reduce room for maneuver. The consequence of a decision can therefore also be observed through the capacity it preserves or eliminates for subsequent decisions.

Reversibility is relevant at this point. A decision that is easy to undo produces different consequences from a decision that requires significant effort or cost to reverse. This does not mean that reversible decisions are always better, but that their consequence structure is different.

Time makes this dynamic even more evident. Delaying a choice may allow new information to emerge, but it may also cause an opportunity to disappear, consume resources, or allow other decisions to be made first.

Remaining in the current state does not mean remaining with the same alternatives. The context itself continues to evolve, and the absence of a decision may cause certain options to become more expensive, infeasible, or simply cease to exist.

It is in this sense that deliberately not deciding can also constitute a decision. There is a difference between consciously choosing not to act and simply failing to perceive that a decision needed to be made, but both situations can affect future possibilities.

The fifth need produced by this foundation is to understand, address, and communicate the consequences of the alternatives under consideration. This involves analyzing not only which alternative produces a given outcome, but also what direct and indirect effects it may generate, who may be affected, how these effects need to be communicated, and how the decision modifies the conditions for subsequent decisions.

Scenarios, alternative analysis, trade-offs, communication, coordination, reversibility, dependencies, opportunity cost, optionality, and path dependency are different ways of addressing this need.

The objective is not to find a universally better alternative. It is to understand how each alternative responds to the existing objectives and constraints, what consequences it produces, who may be affected, and how these consequences alter the space of possibilities for the future.

## 1.6. Every decision participates in a process of evolution

A decision modifies the subsequent situation because its consequences alter the space of possibilities. Resources may be consumed or created, commitments may be made, dependencies may arise, alternatives may be eliminated or opened, and new information may be produced.

This alteration of the space of possibilities changes the conditions that will be observed for subsequent decisions. The context may change, some objectives may become infeasible or gain importance, new uncertainties may emerge or disappear, and other alternatives may come to exist.

This is the sense in which this guide uses the term evolution. Evolution means a change of state over time as a consequence of decisions, actions taken, information produced, and changing conditions. It does not necessarily imply improvement.

A system may move closer to its objectives, but it may also accumulate constraints, dependencies, costs, or problems that make subsequent changes more difficult. An organization may learn from a decision while simultaneously taking on commitments that constrain its next choices.

Planning, execution, observation, and learning are part of this dynamic. A decision may be maintained, revised, or replaced as new data emerges and as the conditions for new choices change.

Models such as PDCA and OODA represent different ways of organizing cycles of this type. They are not Decision Architecture models, but they help illustrate a dynamic in which action, observation, learning, and change are related.

When this process is repeated, previous choices begin to influence subsequent ones. They generate dependencies, commitments, constraints, and learning that become part of the conditions for future choices.

This accumulation also appears in systems architecture. The current architecture can be seen as the result of many decisions made over time, some deliberate and others conditioned by the circumstances that existed.

An architectural decision, for example, may introduce a technology. That technology then influences the hiring of professionals, the choice of tools, operational costs, and integration decisions. An initial decision therefore participates in shaping the conditions for subsequent decisions.

This means that a decision should not be analyzed only based on the state existing at the moment it is made. We also need to consider the effects it produces on the space of possibilities, the conditions of future decisions, and the knowledge it generates.

The sixth need produced by this foundation is the observation, learning, and preservation of the knowledge produced by evolution.

We need to be able to observe what happened, compare the outcome with what we expected, and understand the reasons for any differences.

We also need to be able to retrieve relevant information about previous decisions when new decisions depend on them. This does not mean documenting everything. It means preserving what will be necessary to understand relevant decisions in the future.

Depending on the domain, this can be done through indicators, feedback, retrospectives, decision records, documentation, experiments, or other learning mechanisms.

Traceability emerges as a way of preserving this knowledge, but it is not the objective in itself. The objective is to maintain the ability to understand evolution and use the knowledge produced to guide future decisions.

## 1.7. How the foundations relate to one another

The six foundations proposed in this guide should not be interpreted as six independent subjects. They describe different dimensions of the same decision structure.

A decision occurs in a domain, but that domain always manifests itself within a specific context. The context defines conditions that influence what can be done. Within these conditions, there are objectives that guide the choice. Because the future is not completely known, there is uncertainty. The decision produces direct and indirect consequences, which can affect people, resources, systems, and the conditions for future decisions. These consequences alter the space of possibilities and, in doing so, modify the conditions under which new decisions will be made. This is the process through which evolution occurs.

Thus, we can visualize this relationship as follows:

Domain → context → objectives → uncertainty → consequences → evolution

The sequence does not represent a series of steps. It represents a relationship between dimensions that continuously influence one another.

New information about the domain can change our understanding of the context. A change in context can make an objective infeasible or reveal another that is more important. A different objective can change which alternatives are considered. New evidence can reduce uncertainty. A decision can produce consequences that eliminate a future alternative or create a new possibility. These changes modify the space of possibilities and, consequently, the conditions available for subsequent decisions. An unexpected outcome can also change the context again and require a new understanding of the situation.

A decision therefore does not take place within a static structure. It takes place within a structure that changes as we learn, choose, and act.

This relationship helps explain why different practices and frameworks can appear so different and yet address related needs.

We can establish a second relationship:

Characteristic → need → practice → framework

The domain produces the need for delimitation. This need can be addressed through practices involving boundary definition, modeling, scope, and a common language. DDD, for example, offers practices for understanding and delimiting domains, establishing models, and defining bounded contexts. Other architecture, management, and business analysis approaches also have practices intended to make explicit the boundaries of what is being analyzed.

Context produces the need to make existing conditions explicit. This may involve gathering constraints, assumptions, dependencies, the current situation, stakeholders, and available resources. arc42 explicitly addresses context and scope, constraints, and solution strategy. TOGAF also structures activities related to understanding the environment, architecture, and transition. In projects, planning and diagnostic practices fulfill similar functions.

Objectives produce the need for evaluation criteria. Requirements, metrics, indicators, quality attributes, and success criteria are some of the possible ways to address this need. Scrum uses Product Goal and Sprint Goal to guide the work. PMBOK addresses objectives, planning, delivery, and measurement. In architecture, functional requirements, quality attributes, and constraints help establish references for evaluating alternatives.

Uncertainty produces the need to deal with what we do not yet know. In this case, we can use risk analysis, hypothesis formulation, experimentation, prototyping, research, scenarios, or other investigative practices. Lean Startup uses experimentation and learning to test hypotheses. Design Thinking uses investigation, ideation, prototyping, and testing to learn about needs and possible solutions. Risk management practices address uncertain events and their possible consequences.

Consequences produce the need to analyze their effects and address those that need to be considered by the decision. This includes understanding direct and indirect impacts, identifying who may be affected, communicating relevant changes, coordinating resulting actions, and evaluating how the decision modifies the conditions for future choices. At this point, practices such as scenario analysis, alternative comparison, trade-off identification, reversibility analysis, dependency assessment, communication, and coordination emerge. In planning, different execution options can be compared according to their impacts, costs, risks, and commitments.

Evolution produces the need to observe results, learn, and preserve knowledge. Scrum incorporates inspection and adaptation. Lean Startup structures build-measure-learn cycles. Retrospectives make it possible to examine the experience of one cycle and adjust the next. ADRs preserve knowledge about decisions that continue to influence architectural evolution. Other methods and practices use different mechanisms to address the same fundamental need.

These examples do not mean that each framework belongs to only one foundation. That would be an excessively rigid interpretation. A framework may address several needs at the same time because a practice often operates across more than one dimension of a decision.

Scrum, for example, does not address only evolution. Its objectives guide the work, its inspection mechanisms produce information, and its adaptation allows decisions to be revised as new evidence emerges. Lean Startup does not address only uncertainty. Its cycles also connect objectives, evidence, outcomes, and evolution. arc42 does not address only documentation. Its structure relates context, objectives, constraints, quality, decisions, risks, and architectural knowledge.

The same applies to architecture practices. An architectural decision needs to consider the domain in which the system exists, current conditions, quality and business objectives, technical uncertainties, available alternatives, and the consequences that the architecture will carry over time.

Therefore, the framework does not need to be the starting point. It can be a response to a need that has already been identified.

This inversion is important. Instead of asking first, “which framework should we use?”, we can begin by asking: “what decision are we trying to conduct?”, “which characteristics of this decision need to be addressed?”, “what needs arise from these characteristics?” and, only then, “which practices or frameworks can help us?”.

The six foundations proposed in this guide therefore do not seek to replace DDD, TOGAF, arc42, Scrum, PMBOK, Lean Startup, Design Thinking, ADR, or other methods. They offer a way of seeing what these approaches are trying to address and recognizing that different disciplines can develop distinct responses to structurally related needs.

This perspective will be important in the following chapters. After understanding the general characteristics of a decision, we need to enter the concrete situation in which it takes place. Before defining which problem to solve or which solution to apply, we need to understand the domain, context, boundaries, and existing conditions.

It is from there that Decision Architecture ceases to be merely a conceptual structure and begins to guide the conduct of a real decision.
