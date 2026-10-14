---
layout: single
permalink: /
title: "Mengzhe Geng"
author_profile: true
classes: wide
---

<p class="eyebrow">Research Scientist <span aria-hidden="true">·</span> <a href="https://nrc.canada.ca/en">National Research Council Canada</a></p>

<p class="lede">I study how machine learning systems can <strong>understand and generate speech and audio, adapt across speakers, languages, and modalities, and reason from incomplete evidence</strong>.</p>
<ul class="research-summary">
  <li>My work develops and evaluates accessible speech recognition, low-resource language technologies, speaker adaptation, efficient speech foundation models, and spoken agents.</li>
  <li>I also study multimodal systems that use audio and visual information for prediction and reasoning, asking when they should gather more evidence, answer, act, or abstain.</li>
</ul>

<p class="profile-actions"><a class="button-link" href="/publications/">Browse publications</a> <a href="{{ site.author.googlescholar }}">Full Google Scholar profile <span aria-hidden="true">↗</span></a></p>

<div class="scholar-stats" aria-label="Google Scholar metrics">
  <div class="stat"><strong>{{ site.data.scholar_metrics.citations }}</strong><span>citations</span></div>
  <div class="stat"><strong>{{ site.data.scholar_metrics.h_index }}</strong><span>h-index</span></div>
  <div class="stat"><strong>{{ site.data.scholar_metrics.i10_index }}</strong><span>i10-index</span></div>
</div>
<p class="stats-note">Google Scholar metrics, last refreshed {{ site.data.scholar_metrics.updated_at | date: "%b %-d, %Y" }}</p>

<p class="availability-notice"><strong>I am open to opportunities in both academia and industry. I am authorized to work in Canada, Hong Kong, and Mainland China. If you know of a good fit, <a href="mailto:tim.geng.cuhk@gmail.com">contact me</a>.</strong></p>
<p class="collaboration-invitation">Every student who completed a four-month internship with me coauthored at least <strong>one peer-reviewed publication in a top-tier journal or conference</strong>. I welcome students worldwide for <strong>remote internships</strong> and researchers for <strong>in-person guest researcher opportunities</strong>. Students in Canada can also apply through the NRC <a href="https://www.nrc.canada.ca/en/corporate/careers/nrc-co-op-program" target="_blank" rel="noopener noreferrer">Co-op Program</a> or <a href="https://nrc.canada.ca/en/corporate/careers/nrc-student-employment-program" target="_blank" rel="noopener noreferrer">Student Employment Program</a>. Students: email a CV and transcripts from your bachelor's onward; researchers: a CV. Contact me at <a href="mailto:tim.geng.cuhk@gmail.com">tim.geng.cuhk@gmail.com</a>.</p>
<details class="internship-note">
  <summary>Internships are highly competitive</summary>
  <p>With limited capacity and a high volume of inquiries, I may not be able to reply to everyone. Thank you for your interest; I may contact you about future opportunities.</p>
</details>

<h2 id="experience">Experience</h2>
<div class="timeline-entry">
  <div class="timeline-date">Nov 2023–present</div>
  <div><h3>Research Scientist</h3><p><a href="https://nrc.canada.ca/en/research-development/research-collaboration/research-centres/digital-technologies-research-centre">Digital Technologies</a>, <a href="https://nrc.canada.ca/en">National Research Council Canada</a> · Ottawa, Canada</p></div>
</div>

<h2>Education</h2>
<div class="timeline-entry">
  <div class="timeline-date">2019–2023</div>
  <div><h3><a href="https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-systems-engineering-and-engineering-management" target="_blank" rel="noopener noreferrer">Ph.D. in Systems Engineering and Engineering Management</a></h3><p><a href="https://www.cuhk.edu.hk/english/" target="_blank" rel="noopener noreferrer">The Chinese University of Hong Kong</a></p></div>
</div>
<div class="timeline-entry">
  <div class="timeline-date">2015–2019</div>
  <div><h3><a href="https://www.ie.cuhk.edu.hk/programmes/bsc-in-mieg/" target="_blank" rel="noopener noreferrer">B.Sc. in Mathematics and Information Engineering</a></h3><p><a href="https://www.cuhk.edu.hk/english/" target="_blank" rel="noopener noreferrer">The Chinese University of Hong Kong</a> · <a href="https://www.cuhk.edu.hk/clear/qm/A5-2.pdf" target="_blank" rel="noopener noreferrer">First-class honours</a> · <a href="https://www.erg.cuhk.edu.hk/iris/Elite" target="_blank" rel="noopener noreferrer">ELITE Stream graduate</a> · <a href="https://www.cse.cuhk.edu.hk/academics/minor-computer-science/" target="_blank" rel="noopener noreferrer">Minor in Computer Science</a></p></div>
</div>

<h2 id="research">Research</h2>
{% assign research_themes = site.data.research_themes %}
<div class="research-grid">
  {% for theme in research_themes %}
  <section class="research-card" data-research-theme="{{ theme.label | slugify }}" style="--research-theme-color-light: {{ theme.color }}; --research-theme-color-dark: {{ theme.dark_color }}">
    <span class="research-label">{{ theme.label }}</span>
    <h3>{{ theme.heading }}</h3>
    <p>{{ theme.description }}</p>
  </section>
  {% endfor %}
</div>

<h2 id="author-led-publications">Author-led publications</h2>
{% assign author_led_publications = site.publications | where_exp: "post", "post.author_role" | sort: "scholar_sort_order" %}
{% assign author_led_years = author_led_publications | group_by: "year" | sort: "name" | reverse %}
{% assign timeline_themes = site.data.research_themes %}
{% assign first_timeline_year = author_led_publications | map: "year" | sort | first | plus: 0 %}
{% assign last_timeline_year = site.time | date: "%Y" | plus: 0 %}
{% assign timeline_years = (first_timeline_year..last_timeline_year) %}
<details class="author-led-disclosure">
  <summary><span class="disclosure-label--collapsed">Show timeline and publications ({{ author_led_publications.size }})</span><span class="disclosure-label--expanded">Hide timeline and publications ({{ author_led_publications.size }})</span></summary>
<p class="publication-intro">These include publications for which I am a first author, co-first author, or (joint) corresponding author.</p>
<div class="timeline-scroller" tabindex="0" aria-label="Scrollable publication timeline">
  <div class="research-timeline" style="--timeline-year-count: {{ timeline_years.size }}">
    <div class="timeline-axis"><span class="timeline-axis-label">Research theme</span>{% for year in timeline_years %}<span class="timeline-year">{{ year }}</span>{% endfor %}</div>
    {% for theme in timeline_themes %}
    {% assign theme_slug = theme.label | slugify %}
    <div class="timeline-row" data-timeline-theme="{{ theme_slug }}" style="--timeline-color-light: {{ theme.color }}; --timeline-color-dark: {{ theme.dark_color }}">
      <span class="timeline-row-label">{{ theme.label }}</span>
      {% for year in timeline_years %}
      {% assign year_number = year | plus: 0 %}
      {% assign theme_label = theme.label %}
      {% assign year_theme_publications = author_led_publications | where: "year", year_number | where: "timeline_theme", theme_label %}
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
  {% for theme in timeline_themes %}<button class="publication-filter" type="button" data-publication-filter="{{ theme.label | slugify }}" aria-pressed="false">{{ theme.label }}</button>{% endfor %}
</div>
<p class="publication-filter-status" aria-live="polite">{{ author_led_publications.size }} publications</p>
{% for year_group in author_led_years %}
{% assign latest_author_led_publications = year_group.items | where_exp: "post", "post.latest_work" %}
{% assign dated_author_led_publications = year_group.items | where_exp: "post", "post.publication_date" | where_exp: "post", "post.latest_work != true" | sort: "publication_date" | reverse %}
{% assign year_only_author_led_publications = year_group.items | where_exp: "post", "post.publication_date == nil" | where_exp: "post", "post.latest_work != true" | sort: "scholar_sort_order" %}
{% assign year_ordered_author_led_publications = latest_author_led_publications | concat: dated_author_led_publications | concat: year_only_author_led_publications %}
{% for post in year_ordered_author_led_publications %}
{% assign displayed_authors = post.homepage_authors | default: post.authors %}
<article class="publication-entry author-led-publication" id="author-publication-{{ post.scholar_rank }}" data-publication-theme="{{ post.timeline_theme | slugify }}">
  <h3><a href="{{ post.paperurl | default: post.scholarurl }}" target="_blank" rel="noopener">{{ post.title }}</a></h3>
  <p class="publication-meta">{% include publication-authors.html authors=displayed_authors %} <span aria-hidden="true">·</span> <em>{% include publication-venue-year.html venue=post.venue year=post.year category=post.category append_year=true %}</em></p>
  {% if post.publication_status %}<p class="publication-meta publication-status"><strong>Status:</strong> {{ post.publication_status | escape }}</p>{% endif %}
  <p class="publication-theme-line">{% include publication-theme-label.html %}</p>
  {% include publication-actions.html %}
</article>
{% endfor %}
{% endfor %}
<script defer src="{{ '/assets/js/publication-timeline.js' | prepend: base_path }}"></script>
<script defer src="{{ '/assets/js/publication-citations.js' | prepend: base_path }}"></script>
<p class="more-link"><a href="/publications/">View the full publication list <span aria-hidden="true">→</span></a> <span aria-hidden="true">·</span> <a href="{{ site.author.googlescholar }}">All publications on Google Scholar</a></p>
</details>

<h2 id="researchpod">ResearchPod</h2>
<article class="publication-entry">
  <h3><a href="https://researchpod.app/episode/3ce339ad-82ad-43c2-9051-aa5da401acfb" target="_blank" rel="noopener noreferrer">VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis</a></h3>
  <p class="publication-meta">ResearchPod episode</p>
</article>

<h2 id="huggingface-daily-papers">Hugging Face Daily Papers</h2>
<details class="daily-papers-disclosure">
  <summary><span class="daily-papers-count">2 papers</span><span class="daily-papers-date">Featured Oct 14, 2026</span></summary>
  <div class="daily-papers-list">
    <article class="daily-papers-entry">
      <h3><a href="https://huggingface.co/papers/2610.10808" target="_blank" rel="noopener noreferrer">Controlled Acquisition and Abstention in Three-Channel Score Conflicts</a></h3>
      <p class="publication-meta">{% include publication-authors.html authors="Mengzhe Geng" %} <span aria-hidden="true">·</span> <a href="https://arxiv.org/abs/2610.10808" target="_blank" rel="noopener noreferrer">arXiv:2610.10808</a></p>
    </article>
    <article class="daily-papers-entry">
      <h3><a href="https://huggingface.co/papers/2610.15327" target="_blank" rel="noopener noreferrer">CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks</a></h3>
      <p class="publication-meta">{% include publication-authors.html authors="Mengzhe Geng, Max W. Y. Lam, Yuewen Cao, Shoukang Hu, Jing Xu, Marc Tessier, Xu Li" %} <span aria-hidden="true">·</span> <a href="https://arxiv.org/abs/2610.15327" target="_blank" rel="noopener noreferrer">arXiv:2610.15327</a></p>
    </article>
  </div>
</details>

<h2 id="student-supervision">Student Supervision</h2>
<p class="supervision-intro">Every student who completed a four-month internship with me coauthored at least <strong>one peer-reviewed publication in a top-tier journal or conference</strong>.</p>
<div class="supervision-list">
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Sunyi Liu</span>
      <span class="publication-meta">Undergraduate intern, NRC (UofT) · May–Aug 2024</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Funding</span><span class="supervision-detail-copy"><a class="person-link" href="https://www.nrc.canada.ca/en/corporate/corporate-overview/rebecca-hart" target="_blank" rel="noopener noreferrer">Rebecca Hart</a></span></p>
      <p class="supervision-detail"><span class="supervision-label">Award</span><span class="supervision-detail-copy"><strong>NRC Outstanding Student Contribution Award</strong> (2024)</span></p>
      <p class="supervision-detail"><span class="supervision-label">Publication</span><span class="supervision-detail-copy"><a href="https://ieeexplore.ieee.org/document/11004431" target="_blank" rel="noopener noreferrer">Exploring Generative Artificial Intelligence Techniques in Government: A Case Study</a>, <em>IEEE Intelligent Systems</em> (2025)</span></p>
    </div>
  </details>
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Shenran Wang</span>
      <span class="publication-meta">Undergraduate intern, NRC (UBC) · May–Aug 2025</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Co-supervision</span><span class="supervision-detail-copy"><a class="person-link" href="https://www.nrc.canada.ca/en/corporate/contact-us/nrc-directory-science-professionals/aidan-pine" target="_blank" rel="noopener noreferrer">Aidan Pine</a></span></p>
      <p class="supervision-detail"><span class="supervision-label">Publication</span><span class="supervision-detail-copy"><a href="https://aclanthology.org/2026.eacl-short.16/" target="_blank" rel="noopener noreferrer">Exploring Cross-Lingual Voice Conversion Methods for Anonymizing Low-Resource Text-to-Speech</a>, <em>European Chapter of the Association for Computational Linguistics (EACL 2026)</em></span></p>
    </div>
  </details>
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Changbing Yang</span>
      <span class="publication-meta">Ph.D. intern, NRC (UBC) · May–Aug 2025</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Co-supervision</span><span class="supervision-detail-copy"><a class="person-link" href="https://nrc.canada.ca/en/corporate/contact-us/nrc-directory-science-professionals/patrick-littell" target="_blank" rel="noopener noreferrer">Patrick Littell</a></span></p>
      <p class="supervision-detail"><span class="supervision-label">Award</span><span class="supervision-detail-copy"><strong>NRC Outstanding Student Contribution Award</strong> (2025)</span></p>
      <p class="supervision-detail"><span class="supervision-label">Publication</span><span class="supervision-detail-copy"><a href="https://aclanthology.org/2026.lrec-1.709/" target="_blank" rel="noopener noreferrer">GlossMATE: Multi-Agent Translator Explanations for Glosses</a>, <em>Language Resources and Evaluation Conference (LREC 2026)</em></span></p>
    </div>
  </details>
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Timothy Tse</span>
      <span class="publication-meta">M.Sc. intern, NRC (UBC) · Jul–Oct 2025</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Co-supervision</span><span class="supervision-detail-copy"><a class="person-link" href="https://www.nrc.canada.ca/en/corporate/contact-us/nrc-directory-science-professionals/aidan-pine" target="_blank" rel="noopener noreferrer">Aidan Pine</a> and <a class="person-link" href="https://linguistics.ubc.ca/profile/jian-zhu/" target="_blank" rel="noopener noreferrer">Jian Zhu</a></span></p>
      <p class="supervision-detail"><span class="supervision-label">Award</span><span class="supervision-detail-copy"><strong>NRC Outstanding Student Contribution Award</strong> (2025)</span></p>
      <p class="supervision-detail"><span class="supervision-label">Publication</span><span class="supervision-detail-copy"><a href="https://www.isca-archive.org/interspeech_2026/tse26_interspeech.html" target="_blank" rel="noopener noreferrer">AudioNoisePrints: Model-Free Audio Watermarking Using Spatial Correlation in Flow Matching TTS</a>, <em>INTERSPEECH 2026</em></span></p>
    </div>
  </details>
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Jinxin Ji</span>
      <span class="publication-meta">Remote Ph.D. intern, PolyU · Jul 2026–present · Incoming visiting researcher, Jan 2027</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Preprint</span><span class="supervision-detail-copy"><a href="https://arxiv.org/abs/2609.26823" target="_blank" rel="noopener noreferrer">Text Scores Do Not Establish Performance on Lexically Non-Diagnostic Speech Tasks: A Qwen2-Audio Quantization Case Study</a>, <em>arXiv:2609.26823</em> (2026)</span></p>
    </div>
  </details>
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Yujia Lu</span>
      <span class="publication-meta">Remote undergraduate intern, CUHK · Aug 2026–present</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Preprint</span><span class="supervision-detail-copy"><a href="https://arxiv.org/abs/2609.08899" target="_blank" rel="noopener noreferrer">From Scores to Evidence: Auditable Decisions Can Improve Speech Deepfake Detection</a>, <em>arXiv:2609.08899</em> (2026)</span></p>
    </div>
  </details>
  <details class="supervision-entry">
    <summary class="supervision-heading">
      <span class="supervision-name">Yanfei Lu</span>
      <span class="publication-meta">Incoming Ph.D. intern, NRC (UofT) · Jan 2027</span>
    </summary>
    <div class="supervision-details">
      <p class="supervision-detail"><span class="supervision-label">Publication</span><span class="supervision-detail-copy"><a href="https://aclanthology.org/2026.lrec-1.709/" target="_blank" rel="noopener noreferrer">GlossMATE: Multi-Agent Translator Explanations for Glosses</a>, <em>Language Resources and Evaluation Conference (LREC 2026)</em></span></p>
    </div>
  </details>
</div>

<h2 id="awards">Selected Awards and Honours</h2>
<ul class="award-list">
  <li class="award-item"><strong><a href="https://www.canada.ca/en/government/system/digital-government/gcdigital-community/networking-events/digital-government-community-awards/awards.html" target="_blank" rel="noopener noreferrer">Award for Excellence in Inclusion, Diversity, Equity and Accessibility</a></strong>, Digital Government Community Awards, Government of Canada, 2026 <span class="award-qualifier"><strong>One team recipient per year</strong></span></li>
  <li class="award-item"><strong>Honourable Mention, Outstanding Achievement Award</strong>, NRC Inclusive Innovation Award, National Research Council Canada, 2026 <span class="award-qualifier"><strong>One team recipient per year</strong></span></li>
  <li class="award-item"><strong>IEEE Signal Processing Society Top 25 Downloaded Article (2024–2025),</strong> <a class="award-article-title" href="https://ieeexplore.ieee.org/document/10584335/" target="_blank" rel="noopener noreferrer">“Self-Supervised ASR Models and Features for Dysarthric and Elderly Speech Recognition”</a>, <em>IEEE/ACM Transactions on Audio, Speech, and Language Processing</em>, IEEE Xplore, 2025</li>
  <li class="award-item"><strong>Valedictorian</strong>, <a href="https://www.cpr.cuhk.edu.hk/en/press/cuhk-holds-92nd-congregation-for-the-conferment-of-degrees/" target="_blank" rel="noopener noreferrer">CUHK Postgraduate Class of 2023</a></li>
  <li class="award-item"><strong><a href="https://2023.ieeeicassp.org/outstanding-reviewer-recognitions/" target="_blank" rel="noopener noreferrer">IEEE ICASSP Outstanding Reviewer</a></strong>, 2023</li>
  <li class="award-item"><a href="https://interspeech2023.org/travel-grants/" target="_blank" rel="noopener noreferrer">ISCA INTERSPEECH Travel Grant, 2023</a></li>
  <li class="award-item"><a href="https://www.hkxfoundation.org/aboutus" target="_blank" rel="noopener noreferrer">Finalist, Hong Kong X Foundation FYP+ Project, 2019</a></li>
  <li class="award-item">CUHK Academic Excellence Scholarship for Non-local Students, 2019</li>
  <li class="award-item"><strong>CUHK Best Project Award for Undergraduate Research Summer Internship</strong>, 2018</li>
  <li class="award-item"><strong><a href="https://www3.erg.cuhk.edu.hk/erg/Elite/Scholarship" target="_blank" rel="noopener noreferrer">CUHK ELITE Stream Student Scholarship</a></strong>, 2019 and 2016</li>
  <li class="award-item">CUHK S.H. Ho College Outstanding Student Scholarship, 2018, 2017, 2016, and 2015</li>
  <li class="award-item"><a href="https://admission.cuhk.edu.hk/fees-financing-your-studies/scholarships/reaching-out-award/" target="_blank" rel="noopener noreferrer">HKSAR Government Reaching Out Award</a>, 2018</li>
  <li class="award-item"><strong><a href="https://admission.cuhk.edu.hk/fees-financing-your-studies/scholarships/talent-development-sch/" target="_blank" rel="noopener noreferrer">HKSAR Government Talent Development Scholarship (Innovation)</a></strong>, 2017</li>
  <li class="award-item"><strong><a href="https://www.theiet.org/impact-society/awards-prizes-and-scholarships/iet-student-prizes" target="_blank" rel="noopener noreferrer">The IET Prize</a></strong>, the Institute of Engineering and Technology, 2017</li>
  <li class="award-item"><strong><a href="https://www.csclf.org/" target="_blank" rel="noopener noreferrer">The Soong Ching Ling Foundation Zhiyuan Scholarship</a></strong>, 2015</li>
</ul>

<h2>Profiles</h2>
<p>For the complete publication record, visit <a href="{{ site.author.googlescholar }}">Google Scholar</a> or browse the <a href="{{ '/publications/' | relative_url }}">Publications page</a>.</p>
