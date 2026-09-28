# 2. Understanding the Domain of a Decision

Imagine a biologist studying a species. To understand its characteristics and behavior, they do not observe only the individual. They also need to consider the ecosystem in which it lives, the organisms with which it interacts, the resources on which it depends, and the conditions that influence its existence.

The same principle applies to a decision. A decision may have a specific object, but that object is embedded in a broader reality. People, organizations, processes, systems, resources, rules, and other elements establish relationships with what is being decided and may influence its evolution.

The domain corresponds to the portion of this reality that is relevant to the decision. It does not represent everything that exists, but it is also not necessarily limited to the most obvious object of the decision.

This perspective helps distinguish domain from context. The domain provides a broader view of the reality related to the decision. Context represents the specific conditions under which it is considered. An organization, for example, may be part of the domain, while a budgetary condition, a regulatory change, or a market opportunity may characterize the context in which the decision occurs. The distinction lies mainly in the level of observation, not in the nature of the elements.

This difference between knowing a practice and knowing the reality in which it will be applied explains a recurring problem in professional practice. A professional may master a methodology, follow its rules, and correctly execute its practices. Even so, they may make inadequate decisions by applying them without considering the characteristics of the domain in which they are operating. This is the behavior of a professional who works “by the book”: they transform general guidance into a prescription for a particular reality, as if the methodology also contained the knowledge necessary about the domain.

A project management methodology may guide the planning, monitoring, and control of a project, but it does not, by itself, know the organization’s culture, processes, capabilities, or internal relationships. A solution architecture practice may guide the construction of a solution, but it does not automatically know the organization’s business model, processes, rules, capabilities, or technological constraints. An entrepreneurship technique may guide the investigation of an opportunity, but it does not know the market, customers, competitors, or the specific conditions under which the business will have to exist.

Methods and practices provide general references for action. The domain provides the characteristics of the reality that need to be considered when applying those references.

Understanding the domain does not mean reproducing the entire reality. Just as the biologist does not need to describe the entire ecosystem to study a species, decision architecture needs to represent only what is relevant to the analysis. This work begins by mapping the ecosystem, proceeds to defining its boundaries, and advances to identifying the elements, their characteristics, and their behaviors.

## 2.1. Mapping the ecosystem

A decision does not exist in isolation within an organization. It is embedded in a broader reality formed by the organization itself, the industry in which it operates, the market in which it competes, and the economic, social, technological, and regulatory conditions that influence this environment.

This reality can be understood as an ecosystem: the set of elements and relationships that form the environment in which the decision exists. Not all of these elements will be part of the domain, but knowing them at a sufficient level prevents its boundaries from being defined in an artificially narrow way. The macroeconomic environment may also be part of this view. Inflation, interest rates, employment, income, credit availability, exchange-rate fluctuations, and other economic conditions can alter the behavior of an industry and, consequently, the conditions under which certain decisions are made. The same applies to technological, regulatory, or social changes.

The analogy with the biologist helps clarify this perspective. When studying a species, they consider the available resources, the other organisms, and the relationships they establish with one another. A change in the environment can modify the conditions for the species’ existence, even if its biological characteristics remain the same. In decision architecture, the objective is similar: to recognize the broader reality in which the decision is embedded and identify the elements and relationships that may be relevant to what will be analyzed. It is not necessary to represent the entire ecosystem in detail.

Consider a retail company that decides to replace its sales system. The decision is related to the company’s operations, but the relevant reality is broader. The company operates in a particular industry, competes for customers, depends on suppliers, uses payment methods, contracts logistics services, and is subject to the country’s economic conditions. Consumer behavior, industry practices, labor availability, operating costs, credit conditions, and the level of competition can influence how the company sells its products and, consequently, the characteristics that a new system needs to support.

Within the organization there are also stores, salespeople, customers, products, inventory, payments, logistics, support, systems, and partners. These elements establish relationships with one another and form a reality much larger than the sales system in isolation.

Mapping the ecosystem broadens the field of observation before defining the domain boundaries. As new elements or relationships are identified, this understanding can be revised, also leading to a revision of the domain itself.

## 2.2. Establishing the boundaries of the domain

Recognizing the ecosystem does not mean analyzing all of its elements. The domain corresponds to the portion of this reality that needs to be considered to understand the decision. Establishing its boundaries means determining which parts of the ecosystem will be addressed directly in the analysis and which will remain outside it. This boundary is a conceptual construction: it defines the focus of the investigation, but does not eliminate the relationships that exist beyond the scope.

An element may remain outside the domain and still maintain relevant relationships with what is inside it. The boundary does not make the rest of the ecosystem irrelevant. In decision architecture, it needs to be broad enough to preserve relationships capable of changing the analysis, without incorporating the entire reality.

Consider the retail company again. If the decision involves replacing the sales system, the domain may include salespeople, customers, products, prices, orders, inventory, payments, and the sales system itself. It may also be necessary to consider who makes deliveries, who replenishes inventory, who provides customer support, or who checks suspicious transactions. These elements can directly influence sales operations, even if they are not initially perceived as part of the system.

Defining the boundaries may also reveal that we are dealing with more than one domain. Sales, inventory, logistics, payments, customer service, and fraud prevention may have their own responsibilities, structures, and ways of operating, even though they are related. Another decision then arises: whether to treat these domains jointly or decompose the analysis into related decisions.

This choice can alter the solution architecture. A capability such as fraud verification may be incorporated into a larger system or made available through its own service. Delivery may be part of an integrated solution or use specialized services from partners. Inventory control may reside in the same sales system or in another system related to it.

Therefore, the existing technology architecture does not, by itself, define the boundaries of the domain. A single system may contain capabilities belonging to different parts of reality, just as a single capability may be distributed across multiple systems or services.

Decomposition can also create new related decisions, each with its own boundaries. We therefore have a cycle in which the way a decision is structured influences how its parts will be analyzed.

Organizational culture can influence this choice. Authority structures, professional specializations, incentives, ways of working, and historical patterns of collaboration may favor a more integrated view or a greater separation between parts.

An excessively narrow boundary can hide relationships capable of changing the decision. An excessively broad boundary can make the representation difficult to use. The objective is to find a scope that preserves relevant relationships and allows for clear reasoning.

## 2.3. Identifying the elements of the domain

After establishing the boundaries, it is necessary to recognize which elements make up the domain. The objective is not to produce a complete inventory, but to identify the parts that have sufficient relevance to be treated separately in the decision. This identification depends on the level of abstraction. The same element may be represented as a unit in one analysis and decomposed into smaller parts in another. The appropriate representation is the one that uses the level of detail necessary for the decision.

In the retail company, we can identify customers, salespeople, stores, products, orders, prices, inventory, payments, deliveries, support, fraud verification mechanisms, systems, and partners. The sales system can be treated as a single element when the decision is related to commercial operations as a whole. In a more specific architectural decision, it can be decomposed into applications, services, databases, and integrations.

The same applies to other elements. A store can be represented as a unit or decomposed into teams, equipment, processes, and spaces. A delivery service can be treated as a partner or analyzed in terms of its own capabilities and components.

Decomposition should not occur simply because it is possible to decompose something. It should occur when the current level of abstraction is insufficient for the decision.

When identifying the elements, their relationships also begin to become visible. A salesperson uses the sales system. The system queries product and price information. A sale generates an order. The order may trigger a delivery. Product availability depends on inventory. A transaction may go through payment and fraud verification mechanisms. These relationships may reveal that a particular element, initially considered peripheral, has significant involvement in the decision. In that case, the representation of the domain may need to be revised.

The result of this stage is a structured representation of the main elements of the domain and the level of abstraction appropriate for continuing the analysis.

## 2.4. Understanding characteristics and behaviors

Identifying the elements is still not enough. It is necessary to understand their main characteristics and how they act and interact.

Characteristics describe what the elements are. They may involve nature, purpose, function, capability, composition, structure, or other relevant properties. Behaviors describe how these elements act and interact. An element may respond to certain actions, perform a function, produce information, consume resources, or establish relationships with other elements.

In the retail company, the sales system can be characterized by its purpose, functions, and structure. The salesperson can be described by their activities and capabilities. The product has attributes that need to be presented and recorded. Inventory represents product availability. The delivery service has its own role in moving orders.

Behaviors appear in the interactions between these elements. The salesperson records a sale. The system queries the product and price. Availability is checked in inventory. Payment is forwarded for processing. A transaction may be submitted for fraud verification. Confirmation of the sale may initiate a delivery and update information used by other processes.

These interactions help explain the structural functioning of the domain. A system receives an input and produces a response. A participant performs an action that changes the state of another element. Information is produced in one part and used in another.

The analysis remains, at this point, at a structural level. Specific conditions, constraints, limitations, exceptions, and circumstances that may modify these behaviors belong to a later and more contextualized analysis. The objective is to build a basic understanding of the domain’s structure: which elements exist, what their main characteristics are, and how they relate in general terms. This structure provides the foundation for investigating the specific conditions under which the decision will be made.

## 2.5. Application in project management

A project is an intervention carried out within an organization, a market, and a set of relationships that already exist before it begins. Project management practices therefore need to construct some representation of the reality in which the work will be performed.

This representation appears from the earliest activities. During initiation, it is necessary to understand the organization involved, the people affected, the participating areas, suppliers, existing systems, and their relationships. During planning, this knowledge guides the definition of the work, teams, deliverables, and necessary interfaces.

This need is present in different approaches, even though they use different forms and vocabularies. In the PMBOK, for example, identifying stakeholders, understanding the organizational environment, defining scope, and organizing the work contribute to representing what is involved in the project. In iterative approaches such as Scrum, the domain appears in understanding the product, users, stakeholders, and the reality in which increments will be used. In Kanban, it appears in understanding the workflow, types of work, and relationships between its stages.

The project structure also depends on how its elements are identified. A team can be treated as a unit or analyzed according to its roles and capabilities. A system may appear as an external dependency or be considered part of the work. A supplier may be merely a procurement or a relevant part of the operation that needs to be integrated into the project.

The adopted boundaries influence the very definition of the project. A sales system implementation may consider only the application and its technical team or also involve stores, salespeople, commercial processes, inventory, payments, logistics, and technology suppliers. What changes is not only the size of the project, but the reality within which it will be conducted.

Therefore, stakeholder identification, scope definition, work decomposition, process mapping, and interface identification also function as mechanisms for making the domain observable.

The level of representation required depends on the decision. An organization can be treated as a single element at a given moment and later be decomposed into areas, teams, processes, or systems.

The domain, therefore, is not an artifact specific to a methodology. It is the reality that project management practices need to represent for the work to have meaning.

## 2.6. Application in solution architecture

In solution architecture, the domain occupies a particularly evident position because a solution is built to operate on an existing reality. Systems, integrations, services, and components need to correspond to elements and relationships present in the environment in which they will be used.

Architecture therefore begins before the choice of technologies. The architect needs to recognize which parts of reality are related to the solution, which concepts exist in this space, and how they relate to one another.

Architecture practices use different mechanisms to construct this representation. Domain models, capability maps, process models, context diagrams, system maps, data models, and architecture diagrams represent different aspects of reality. The C4 Model, for example, works with different levels of representation of a system’s structure. arc42 organizes architectural information to make decisions, structures, and relationships explicit. Approaches such as DDD place domain concepts and their boundaries at the center of architecture construction.

These representations also help establish boundaries. A business capability may be supported by a single system or distributed across several. A system may concentrate different capabilities. A functionality that appears to belong to an application may depend on processes, people, or external systems.

Consider again the retail company that intends to replace its sales system. The domain may involve sales, products, prices, inventory, payments, stores, salespeople, and other systems. This reality, however, does not automatically determine a technology architecture. The sales system may remain a single application, be divided into services, or depend on solutions provided by different partners.

The technology architecture is a representation constructed on top of this reality. Therefore, the boundaries of technological components should not be confused with the boundaries of the domain. A service is not necessarily a domain, just as a system does not necessarily correspond to a single business capability.

This distinction is fundamental to practices such as system decomposition, integration definition, data organization, and responsibility distribution. Before deciding how a solution will be structured, it is necessary to understand what exists in the reality that it intends to represent and transform.

## 2.7. Application in user experience

In user experience, the domain is often reduced to the interaction between a person and an interface. This representation is useful for some decisions, but insufficient for many situations involving a usage experience.

An interaction with a product occurs within a service and an organization. Behind a screen there are processes, systems, people, policies, information, and operations that influence what the user can do. Therefore, UX practices need to consider not only the point of contact, but the reality that produces and sustains that experience.

This perspective appears in different practices. User research seeks to understand people and their relationships with the product or service. Journeys represent sequences of interactions throughout an experience. Service maps broaden this view to include activities that occur behind the scenes. Usability testing analyzes interaction within a given scope. Design Thinking and Double Diamond organize investigation, definition, exploration, and development activities that work with different representations of the problem and its environment.

Consider again the sales system of a retail company. Research may show that salespeople have difficulty locating products or completing a sale. An analysis limited to the interface could identify navigation problems or an excessive number of steps. But the experience also depends on inventory, prices, business rules, payment methods, integrated systems, and activities performed by the salesperson. The behavior observed in the interface may result from the interaction among several of these elements.

The boundaries of the investigation therefore depend on the decision. In an analysis of a screen, the user, interface, and information presented may be sufficient. In an analysis of the shopping experience, it may be necessary to include the store, salespeople, inventory, payment, delivery, customer service, and digital channels.

The same applies to the level of abstraction. A user may be treated as a participant or analyzed according to tasks, needs, and forms of interaction. A service may be considered a single experience or decomposed into stages, channels, and backstage activities.

Personas, journey maps, service maps, task flows, prototypes, and usability tests are different ways of representing parts of the domain relevant to an experience. Each makes certain elements visible and leaves others outside its scope.

The quality of an experience therefore does not depend only on the interface. The interface is one element of a larger reality, and UX work needs to determine which part of that reality is relevant to the experience being studied.

## 2.8. Application in entrepreneurship

In entrepreneurship, the domain is the reality in which a business opportunity can exist. It involves customers, competitors, suppliers, channels, partners, technologies, regulations, available capabilities, and market characteristics.

For this reason, entrepreneurship practices often begin by constructing representations of this reality. The Business Model Canvas organizes elements related to customers, value proposition, channels, activities, resources, partners, revenues, and costs. The Value Proposition Canvas focuses on the relationship between a proposition and particular customer segments. Customer Development structures activities for investigating and learning about customers and the market. Lean Startup uses hypotheses, experiments, and learning cycles to obtain evidence about particular parts of the business.

Each approach works with a different scope, and none automatically represents the entire domain of a venture.

Consider a company that intends to create a solution for small retailers. The domain may involve the behavior of these retailers, the systems they use, their suppliers, available payment methods, acquisition channels, competitors, cost structure, and industry conditions.

The boundaries can alter the very interpretation of the opportunity. A solution for large retail chains may belong to a different reality from that found in small establishments, even if the product appears similar. Likewise, an opportunity may exist in a particular industry or region and not present the same conditions elsewhere.

The elements can also be analyzed at different levels. “Customer” can be treated as a segment or decomposed into different profiles. “Competition” can represent a category of alternatives or specific companies. “Market” can be treated as a broad industry or delimited by region, channel, or customer type.

The hypotheses used in entrepreneurship are statements about the domain. When someone states that a particular group has a need, is willing to pay for a solution, or that a particular channel allows acquisition at scale, they are formulating a hypothesis about an external reality.

Experiments, interviews, value proposition tests, and initial launches make it possible to observe parts of this reality. The knowledge produced is associated with the investigated scope: evidence obtained from a particular segment, region, or channel does not automatically represent all possible customers or markets.

Entrepreneurship frameworks and practices thus provide structures for observing different parts of a business’s domain. The adopted representation influences what can be perceived as an opportunity, market, customer, competitor, or business model.

## 2.9. Application in professional career and personal life

Professional and personal decisions also take place within domains that can be represented and investigated. A career decision, for example, is related to a reality composed of skills, experience, professions, organizations, the labor market, education, location, resources, and professional relationships.

This reality can be represented in different ways depending on the decision. A skills inventory can represent the person based on knowledge and capabilities. An analysis of the labor market can represent opportunities, organizations, professions, and demand. A career map can organize possible paths. A scenario analysis can represent different environments in which a path could occur.

The same principle applies to personal decisions. Moving to another city may involve work, housing, transportation, relationships, services, and resources. Starting a business may involve the market, customers, suppliers, capital, capabilities, and professional relationships. Choosing an educational program may involve institutions, courses, costs, recognition, location, and professional alternatives.

The boundaries vary according to the decision. To choose between two professional specializations, it may be sufficient to represent skills, institutions, costs, and career opportunities. To decide whether to move to another city, it may be necessary to include the labor market, housing, commuting, family relationships, and available services.

The elements can also be decomposed as needed. “Career” can be treated as a trajectory or analyzed in terms of professions, organizations, skills, and opportunities. The “labor market” can be viewed as a general category or divided by industry, region, profession, and experience level.

This perspective does not turn life into an abstract model. It recognizes that every choice takes place within a reality composed of elements that already exist and relate to one another.

Career planning practices, skills analysis, market research, scenario construction, and decision matrices are ways of making parts of this reality more explicit. Each produces a representation appropriate to a particular type of investigation.

The concept of domain, therefore, does not belong exclusively to a technical or business discipline. Project management, solution architecture, user experience, entrepreneurship, career, and personal life use different ways of representing the reality in which their decisions take place. What changes across these areas are the elements considered relevant, the boundaries adopted, the levels of abstraction, and the practices used to construct the representation.

The foundation remains: before deciding about something, it is necessary to recognize the reality to which that decision belongs.
