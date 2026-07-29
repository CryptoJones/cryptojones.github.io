---
layout: post
title: "Why AI Agents Need a Rulebook"
---

<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; margin-bottom:1rem;">
  <iframe src="https://www.youtube.com/embed/Sir59K8ZDPU" title="Why Agentic Systems Need Ontologies by Frank Coyle" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute; top:0; left:0; width:100%; height:100%;"></iframe>
</div>

<div style="margin-bottom:1.5rem;"><strong><a href="https://www.youtube.com/watch?v=Sir59K8ZDPU">Watch Why Agentic Systems Need Ontologies on YouTube</a></strong></div>

Frank Coyle starts with two ideas that grew up far apart. An AI agent is a program that can look at a problem, choose what to do, and take the next step. An ontology is a map of facts and rules for one subject. It lists the things that exist, how they connect, and what each thing is allowed to be. Agents grew out of early work on artificial intelligence. Ontologies reach all the way back to Aristotle and his effort to sort the world into clear groups. Coyle says these two ideas now belong together. Agents bring speed and flexibility. Ontologies give them a shared picture of the world.

This pairing is called neurosymbolic AI. The name sounds harder than the idea. A language model is good at finding likely answers, but likely does not always mean true. An ontology adds facts and rules that the model must answer to. Most ontologies are stored as graphs, which connect pieces of information like dots joined by lines. A company can build one from the top down by asking experts to describe its work. It can also build from the bottom up by studying real orders, customer questions, and other daily events. It can even reuse public systems such as Schema.org instead of naming everything from scratch.

The rules around a graph can uncover facts that were never typed into it. For example, if the graph says that anyone who teaches is a teacher, then the sentence "Bob teaches Scooter" tells the system that Bob is a teacher. If every teacher is also a person, it now knows Bob is a person too. Tools called RDFS and OWL let people write this kind of rule. They can also set limits. An order may have only one final refund, or its status may be paid, shipped, or refunded and nothing else. These checks turn a pile of connected facts into something that can spot bad data.

Those checks matter because agents work in loops. An agent asks a language model what to do, uses a tool, looks at the result, and repeats. The language model does not click buttons or change records by itself. It suggests a tool call and the software carries it out. A loop lets an agent finish a long task, but it can also wander, repeat forever, or burn money through extra token use. Coyle places an ontology check after the tool runs. If the result breaks a rule, the system can try again or ask a person for help. The agent should not make a lasting change until that check passes.

Coyle's examples show why plain English is not enough. A model might approve a second refund for the same order, send money to a support worker instead of a buyer, or invent a status such as "probably shipped." Each answer may sound reasonable even though it breaks the business rules. An ontology can reject those mistakes because the rules are written in a form the computer can test. The larger lesson is not to replace the creative side of a language model. It is to put solid rails around it. Let the agent suggest and explore, then use the ontology to check its work before the result reaches the real world.
