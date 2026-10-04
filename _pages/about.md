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
    <span class="research-label">AI for Healthcare</span>
    <h3>Accessible speech recognition</h3>
    <p>Speech recognition and severity-aware evaluation for dysarthric and older-adult speech under limited data.</p>
  </section>
  <section class="research-card">
    <span class="research-label">AI Safety</span>
    <h3>Evidence-aware and trustworthy speech AI</h3>
    <p>Auditable decisions, deepfake detection, and evaluation methods that make speech systems easier to inspect and trust.</p>
  </section>
  <section class="research-card">
    <span class="research-label">Multimodal Foundation Models</span>
    <h3>Efficient speech foundation models</h3>
    <p>Evaluation, compression, quantization, and adaptation of speech foundation models for practical deployment, including low-resource languages.</p>
  </section>
  <section class="research-card">
    <span class="research-label">Spoken Agents</span>
    <h3>Source-grounded speech generation</h3>
    <p>Spoken agents, audio language models, and speech generation systems that plan, produce, and evaluate audio with explicit evidence.</p>
  </section>
  <section class="research-card">
    <span class="research-label">Reasoning</span>
    <h3>Reasoning and evaluation for generative AI</h3>
    <p>Reasoning systems and evaluation frameworks for generative and multimodal AI in public-sector and research settings.</p>
  </section>
</div>

<h2>Author-led publications</h2>
<p class="publication-intro">These are the publications in which I am listed as first author, last author, or both, based on the author order in the publication record.</p>
{% assign author_led_publications = site.publications | where_exp: "post", "post.author_role" | sort: "author_role_order" %}
{% for post in author_led_publications %}
{% assign publication_url = post.paperurl | default: post.scholarurl %}
{% assign displayed_authors = post.homepage_authors | default: post.authors %}
<article class="publication-entry">
  <h3><a href="{{ publication_url }}" target="_blank" rel="noopener">{{ post.title }}</a></h3>
  <p class="publication-meta">{% include publication-authors.html authors=displayed_authors %} <span aria-hidden="true">·</span> <em>{{ post.venue }}</em>, {{ post.year }}</p>
  <p class="publication-theme-line">{% include publication-theme-label.html %}</p>
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
  <div><h3>B.Sc. in Mathematics and Information Engineering</h3><p>The Chinese University of Hong Kong · First-class honours · ELITE Stream graduate · Minor in Computer Science</p></div>
</div>

<h2 id="awards">Selected awards and honours</h2>
<ul class="award-list">
  <li class="award-item"><strong>Honourable Mention, Outstanding Achievement Award (OAA),</strong> NRC Inclusive Innovation Award, National Research Council Canada, 2026</li>
  <li class="award-item"><strong>Award for Excellence in Inclusion, Diversity, Equity and Accessibility,</strong> Digital Government Community Awards, Canada, 2026</li>
  <li class="award-item"><strong>Valedictorian</strong>, CUHK Postgraduate Class of 2023</li>
  <li class="award-item"><strong>IEEE ICASSP Outstanding Reviewer</strong>, 2023</li>
  <li class="award-item">ISCA INTERSPEECH Travel Grant, 2023</li>
  <li class="award-item">Finalist, Hong Kong X Foundation FYP+ Project, 2019</li>
  <li class="award-item">CUHK Academic Excellence Scholarship for Non-local Students, 2019</li>
  <li class="award-item">CUHK Best Project Award for Undergraduate Research Summer Internship, 2018</li>
  <li class="award-item"><strong>CUHK ELITE Stream Student Scholarship</strong>, 2019 and 2016</li>
  <li class="award-item">CUHK S.H. Ho College Outstanding Student Scholarship, 2018, 2017, 2016, and 2015</li>
  <li class="award-item">HKSAR Government Reaching Out Award, 2018</li>
  <li class="award-item"><strong>HKSAR Government Talent Development Scholarship (Innovation)</strong>, 2017</li>
  <li class="award-item">The IET Prize, the Institute of Engineering and Technology, 2017</li>
  <li class="award-item"><strong>The Soong Ching Ling Foundation Scholarship</strong>, China Soong Ching Ling Foundation, 2015</li>
</ul>

<h2>Profiles</h2>
<p>For the complete publication record, visit <a href="{{ site.author.googlescholar }}">Google Scholar</a>.</p>
