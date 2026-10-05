---
layout: single
permalink: /
title: "Mengzhe Geng"
author_profile: true
classes: wide
---

<p class="eyebrow">Research Scientist <span aria-hidden="true">·</span> National Research Council Canada</p>

<p class="lede">My research develops and evaluates <strong>machine learning for speech, language, audio, and multimodal AI</strong>, including accessible and low-resource speech, speaker adaptation, foundation models, generative and reasoning systems, and trustworthy evaluation.</p>

<p class="profile-actions"><a class="button-link" href="/publications/">Browse publications</a> <a href="{{ site.author.googlescholar }}">Full Google Scholar profile <span aria-hidden="true">↗</span></a></p>

<div class="scholar-stats" aria-label="Google Scholar metrics">
  <div class="stat"><strong>{{ site.data.scholar_metrics.citations }}</strong><span>citations</span></div>
  <div class="stat"><strong>{{ site.data.scholar_metrics.h_index }}</strong><span>h-index</span></div>
  <div class="stat"><strong>{{ site.data.scholar_metrics.i10_index }}</strong><span>i10-index</span></div>
</div>
<p class="stats-note">Google Scholar metrics, last refreshed {{ site.data.scholar_metrics.updated_at | date: "%B %-d, %Y" }}</p>

<p class="availability-notice"><strong>I am open to opportunities in both academia and industry. I can work in Canada, Hong Kong, and Mainland China without needing to apply for an additional work visa. If you know of a good fit, <a href="mailto:tim.geng.cuhk@gmail.com">contact me</a>.</strong></p>

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

<h2 id="author-led-publications">Author-led publications</h2>
<p class="publication-intro">These include publications for which I am a first author, co-first author, or (joint) corresponding author.</p>
{% assign author_led_publications = site.publications | where_exp: "post", "post.author_role" | sort: "author_role_order" %}
{% assign timeline_themes = "Accessible speech AI|Language technology|Trustworthy audio AI|Foundation model evaluation|Speech generation and agents" | split: "|" %}
{% assign first_timeline_year = author_led_publications | map: "year" | sort | first | plus: 0 %}
{% assign last_timeline_year = site.time | date: "%Y" | plus: 0 %}
{% assign timeline_years = (first_timeline_year..last_timeline_year) %}
<div class="timeline-scroller" tabindex="0" aria-label="Scrollable publication timeline">
  <div class="research-timeline" style="--timeline-year-count: {{ timeline_years.size }}">
    <div class="timeline-axis"><span class="timeline-axis-label">Research theme</span>{% for year in timeline_years %}<span class="timeline-year">{{ year }}</span>{% endfor %}</div>
    {% for theme in timeline_themes %}
    {% assign theme_slug = theme | slugify %}
    <div class="timeline-row" data-timeline-theme="{{ theme_slug }}">
      <span class="timeline-row-label">{{ theme }}</span>
      {% for year in timeline_years %}
      {% assign year_number = year | plus: 0 %}
      {% assign year_theme_publications = author_led_publications | where: "year", year_number | where: "timeline_theme", theme %}
      <span class="timeline-cell{% if year_theme_publications.size > 0 %} has-publications{% endif %}" aria-label="{{ year }}: {{ year_theme_publications.size }} publications">
        {% if year_theme_publications.size > 0 %}<span class="timeline-count">{{ year_theme_publications.size }}</span>{% endif %}
        {% for post in year_theme_publications %}<a class="timeline-marker" href="#author-publication-{{ post.scholar_rank }}" title="{{ post.title | escape }}" aria-label="{{ post.title | escape }}"></a>{% endfor %}
      </span>
      {% endfor %}
    </div>
    {% endfor %}
  </div>
</div>
<div class="publication-filters" role="group" aria-label="Filter author-led publications by research theme">
  <button class="publication-filter is-active" type="button" data-publication-filter="all" aria-pressed="true">All</button>
  {% for theme in timeline_themes %}<button class="publication-filter" type="button" data-publication-filter="{{ theme | slugify }}" aria-pressed="false">{{ theme }}</button>{% endfor %}
</div>
<p class="publication-filter-status" aria-live="polite">{{ author_led_publications.size }} publications</p>
{% for post in author_led_publications %}
{% assign displayed_authors = post.homepage_authors | default: post.authors %}
<article class="publication-entry author-led-publication" id="author-publication-{{ post.scholar_rank }}" data-publication-theme="{{ post.timeline_theme | slugify }}">
  <h3><a href="{{ post.paperurl | default: post.scholarurl }}" target="_blank" rel="noopener">{{ post.title }}</a></h3>
  <p class="publication-meta">{% include publication-authors.html authors=displayed_authors %} <span aria-hidden="true">·</span> <em>{{ post.venue }}</em>, {{ post.year }}</p>
  <p class="publication-theme-line">{% include publication-theme-label.html %}</p>
  {% include publication-actions.html %}
</article>
{% endfor %}
<script defer src="{{ '/assets/js/publication-timeline.js' | prepend: base_path }}"></script>
<p class="more-link"><a href="/publications/">View the full publication list <span aria-hidden="true">→</span></a> <span aria-hidden="true">·</span> <a href="{{ site.author.googlescholar }}">All publications on Google Scholar</a></p>

<h2 id="awards">Selected awards and honours</h2>
<ul class="award-list">
  <li class="award-item"><strong>Honourable Mention, Outstanding Achievement Award (OAA),</strong> NRC Inclusive Innovation Award, National Research Council Canada, 2026</li>
  <li class="award-item"><strong>Award for Excellence in Inclusion, Diversity, Equity and Accessibility,</strong> Digital Government Community Awards, Government of Canada, 2026</li>
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
  <li class="award-item"><strong>The IET Prize</strong>, the Institute of Engineering and Technology, 2017</li>
  <li class="award-item"><strong>The Soong Ching Ling Foundation Scholarship</strong>, China Soong Ching Ling Foundation, 2015</li>
</ul>

<h2>Profiles</h2>
<p>For the complete publication record, visit <a href="{{ site.author.googlescholar }}">Google Scholar</a> or browse the <a href="{{ '/publications/' | relative_url }}">Publications page</a>.</p>
