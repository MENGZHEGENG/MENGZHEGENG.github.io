---
layout: single
permalink: /
title: "Mengzhe Geng"
author_profile: true
classes: wide
---

<p class="eyebrow">Research Scientist <span aria-hidden="true">·</span> National Research Council Canada</p>

<p class="lede">I build speech and language technologies for people and languages that are often underserved by mainstream AI.</p>

<p>My research spans speech recognition and adaptation for dysarthric and older-adult speech, speech technologies for Canadian Indigenous and other low-resource languages, and the evaluation of speech and multimodal foundation models. I also work on reasoning systems and generative AI in public-sector settings.</p>

<p class="profile-actions"><a class="button-link" href="/publications/">Browse publications</a> <a href="{{ site.author.googlescholar }}">Full Google Scholar profile <span aria-hidden="true">↗</span></a></p>

<div class="scholar-stats" aria-label="Google Scholar metrics">
  <div class="stat"><strong>1,664</strong><span>citations</span></div>
  <div class="stat"><strong>23</strong><span>h-index</span></div>
  <div class="stat"><strong>31</strong><span>i10-index</span></div>
</div>
<p class="stats-note">Google Scholar snapshot, October 2026</p>

<h2 id="research">Research</h2>
<div class="research-grid">
  <section class="research-card">
    <h3>Speech, health and accessibility</h3>
    <p>Recognition and speaker adaptation for dysarthric and older-adult speech, with a focus on robust systems under limited data.</p>
  </section>
  <section class="research-card">
    <h3>Indigenous and low-resource languages</h3>
    <p>Speech recognition and language technologies that support documentation and learning for Canadian Indigenous languages.</p>
  </section>
  <section class="research-card">
    <h3>Foundation models and responsible AI</h3>
    <p>Speech and multimodal foundation models, reasoning, spoken agents, AI safety, and generative AI in government.</p>
  </section>
</div>

<h2>Selected publications</h2>
{% assign featured_publications = site.publications | where: "featured", true | sort: "sort_order" %}
{% for post in featured_publications %}
<article class="publication-entry">
  <h3><a href="{{ post.paperurl }}" target="_blank" rel="noopener">{{ post.title }}</a></h3>
  <p class="publication-meta">{{ post.homepage_authors | default: post.authors | escape }} <span aria-hidden="true">·</span> <em>{{ post.venue }}</em>, {{ post.year }}</p>
</article>
{% endfor %}
<p class="more-link"><a href="/publications/">View the full publication list <span aria-hidden="true">→</span></a> <span aria-hidden="true">·</span> <a href="{{ site.author.googlescholar }}">All publications on Google Scholar</a></p>

<h2 id="experience">Experience</h2>
<div class="timeline-entry">
  <div class="timeline-date">Nov 2023–present</div>
  <div><h3>Research Scientist</h3><p>Digital Technologies, National Research Council Canada · Ottawa, Canada</p></div>
</div>

<h2>Education</h2>
<div class="timeline-entry">
  <div class="timeline-date">2019–2023</div>
  <div><h3>Ph.D. in Systems Engineering and Engineering Management</h3><p>The Chinese University of Hong Kong</p></div>
</div>
<div class="timeline-entry">
  <div class="timeline-date">2015–2019</div>
  <div><h3>B.Sc. in Mathematics and Information Engineering</h3><p>The Chinese University of Hong Kong · First-class honours · Minor in Computer Science</p></div>
</div>

<h2 id="awards">Awards and honours</h2>
<ul class="award-list">
  <li><strong>Honourable Mention, Outstanding Achievement Award (OAA),</strong> NRC Inclusive Innovation Award, National Research Council Canada, 2026</li>
  <li><strong>Award for Excellence in Inclusion, Diversity, Equity and Accessibility,</strong> Digital Government Community Awards, Canada, 2026</li>
  <li>Valedictorian, CUHK Postgraduate Class of 2023</li>
  <li>ISCA INTERSPEECH Travel Grant, 2023</li>
  <li>CUHK Academic Excellence Scholarship for Non-local Students, 2019</li>
</ul>

<h2>Profiles</h2>
<p>For the complete publication record and current citation metrics, visit <a href="{{ site.author.googlescholar }}">Google Scholar</a>. You can also find me on <a href="https://www.linkedin.com/in/mengzhe-geng-3a6b26115/">LinkedIn</a>.</p>
