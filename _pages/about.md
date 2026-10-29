---
layout: single
permalink: /
title: "Mengzhe Geng"
seo_title: "Mengzhe Geng · Speech AI and Language Technology"
description: "Mengzhe Geng is a Research Scientist at the National Research Council Canada, working on speech AI, low-resource language technology, and multimodal AI."
author_profile: true
classes: wide
show_safety_notice: true
---

{% if page.show_safety_notice %}
<aside id="safety-notice" class="safety-notice" role="region" aria-label="Safety notice">
  <p><strong>Notice.</strong> I'm aware of a recent serious attack on my collaborators, students, and me. Every feasible step will be taken, including legal action where warranted.</p>
  <button class="safety-notice__close" type="button" aria-label="Dismiss safety notice">×</button>
</aside>
<script src="{{ '/assets/js/safety-notice.js' | relative_url }}?v=a748c56" defer></script>
{% endif %}



<p class="eyebrow">Research Scientist <span aria-hidden="true">·</span> <a href="https://nrc.canada.ca/en">National Research Council Canada</a></p>

<p class="lede">My research develops AI for accessible speech, low-resource language technology, adaptive speech models, speech and audio generation, spoken agents, and multimodal reasoning. I also study how AI can serve people and society through interdisciplinary work with linguistics, finance, psychology, media studies, neuroscience, and related fields.</p>

<p class="profile-actions"><a class="button-link" href="/publications/">Browse publications</a> <a href="{{ site.author.googlescholar }}">Google Scholar profile <span aria-hidden="true">↗</span></a></p>
<p class="explore-note">Explore linked papers, programs, and resources.</p>

<div class="scholar-stats" aria-label="Google Scholar metrics">
  <div class="stat"><strong>{{ site.data.scholar_metrics.citations }}</strong><span>citations</span></div>
  <div class="stat"><strong>{{ site.data.scholar_metrics.h_index }}</strong><span>h-index</span></div>
  <div class="stat"><strong>{{ site.data.scholar_metrics.i10_index }}</strong><span>i10-index</span></div>
</div>
<p class="stats-note">Google Scholar metrics, last refreshed {{ site.data.scholar_metrics.updated_at | date: "%b %-d, %Y" }}</p>

<p class="availability-notice"><strong>I welcome opportunities in academia, industry, and startups, and have authorization to work in Canada, Hong Kong, and Mainland China. If you know of an opportunity that might be a good fit, please feel free to <a href="mailto:tim.geng.cuhk@gmail.com">contact me</a>.</strong></p>
<p class="collaboration-invitation">Each student who completed a four-month internship with me coauthored at least <strong>one peer-reviewed paper in a top-tier journal or conference</strong>. Details will be announced later.</p>
<p class="indigenous-community-invitation">Indigenous communities interested in exploring speech and language technologies with the NRC can start by visiting the NRC <a href="https://www.nrc.canada.ca/en/research-development/research-collaboration/programs/indigenous-languages-technology-program" target="_blank" rel="noopener noreferrer">Indigenous Languages Technology (ILT) Program webpage</a> and contacting me at <a href="mailto:Mengzhe.Geng@nrc-cnrc.gc.ca">Mengzhe.Geng@nrc-cnrc.gc.ca</a>.</p>

<h2 id="experience">Experience</h2>
<div class="timeline-entry">
  <div class="timeline-date">Nov 2023–present</div>
  <div><h3>Research Scientist</h3><p><a href="https://nrc.canada.ca/en/research-development/products-services/technical-advisory-services/multilingual-text-processing">Multilingual Text Processing</a>, <a href="https://nrc.canada.ca/en/research-development/research-collaboration/research-centres/digital-technologies-research-centre">Digital Technologies</a>, <a href="https://nrc.canada.ca/en">National Research Council Canada</a></p></div>
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

<h2 id="research">Research Interests</h2>
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
{% comment %}Include first/last authors directly from the author list; retain explicit roles for co-first and corresponding authors. This avoids omissions when a new record lacks author_role metadata.{% endcomment %}
{% assign author_led_publications = "" | split: "," %}
{% for post in site.publications %}
  {% assign publication_authors = post.authors | remove: "*" | remove: "†" | split: "," %}
  {% assign first_author = publication_authors | first | strip %}
  {% assign last_author = publication_authors | last | strip %}
  {% if post.author_role or first_author == "Mengzhe Geng" or first_author == "M. Geng" or first_author == "M Geng" or last_author == "Mengzhe Geng" or last_author == "M. Geng" or last_author == "M Geng" %}
    {% assign author_led_publications = author_led_publications | push: post %}
  {% endif %}
{% endfor %}
{% assign author_led_publications = author_led_publications | sort: "scholar_sort_order" %}
{% assign author_led_years = author_led_publications | group_by: "year" | sort: "name" | reverse %}
{% assign timeline_themes = site.data.research_themes | where_exp: "theme", "theme.show_in_publications != false" %}
{% assign first_timeline_year = author_led_publications | map: "year" | sort | first | plus: 0 %}
{% assign last_timeline_year = site.time | date: "%Y" | plus: 0 %}
{% assign timeline_years = (first_timeline_year..last_timeline_year) %}
<details class="author-led-disclosure">
  <summary><span class="disclosure-label--collapsed">Show timeline and publications ({{ author_led_publications.size }})</span><span class="disclosure-label--expanded">Hide timeline and publications ({{ author_led_publications.size }})</span></summary>
<p class="publication-intro" id="timeline-instructions">Publications where I am first/co-first, (joint) corresponding, or senior/last author. Scroll horizontally for all years; numbers show yearly counts, and dots link to publications.</p>
<div class="timeline-scroller" tabindex="0" role="region" aria-label="Publication timeline by research theme and year" aria-describedby="timeline-instructions">
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
        {% if year_theme_publications.size > 0 %}
        <span class="timeline-count">{{ year_theme_publications.size }}</span>
        <span class="timeline-markers">
        {% for post in year_theme_publications %}<a class="timeline-marker" href="#author-publication-{{ post.scholar_rank }}" title="{{ post.title | escape }}" aria-label="{{ year }}: {{ post.title | escape }}"></a>{% endfor %}
        </span>
        {% endif %}
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
<p>If you find these papers interesting, please consider upvoting them on Hugging Face.</p>
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

<h2 id="awards">Selected Awards and Honours</h2>
<p class="award-section-meta">2015–2026 · 25 awards</p>
<div class="award-groups">
  <details id="award-group-work" class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">Work</span>
        <span class="award-card__meta">2023–2026 · 3 awards</span>
      </span>
    </summary>
    <div class="award-group__content">
        <ul class="award-list">
          <li class="award-item">2026 — <strong><a href="https://www.canada.ca/en/government/system/digital-government/gcdigital-community/networking-events/digital-government-community-awards/awards.html" target="_blank" rel="noopener noreferrer">Award for Excellence in Inclusion, Diversity, Equity and Accessibility</a></strong>, Digital Government Community Awards, Government of Canada <span class="award-qualifier"><strong>One team recipient per year</strong></span></li>
          <li class="award-item">2026 — <strong>Honourable Mention, Outstanding Achievement Award</strong>, the NRC Inclusive Innovation Award, National Research Council Canada <span class="award-qualifier"><strong>One team recipient per year</strong></span></li>
          <li class="award-item">2025 — <strong>IEEE Signal Processing Society Top 25 Downloaded Article (2024–2025),</strong> <a class="award-article-title" href="https://ieeexplore.ieee.org/document/10584335/" target="_blank" rel="noopener noreferrer">“Self-Supervised ASR Models and Features for Dysarthric and Elderly Speech Recognition”</a>, <em>IEEE/ACM Transactions on Audio, Speech, and Language Processing</em>, IEEE Xplore</li>
        </ul>
    </div>
  </details>
  <details id="award-group-postgraduate" class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">Postgraduate</span>
        <span class="award-card__meta">2019–2023 · 4 awards</span>
      </span>
    </summary>
    <div class="award-group__content">
        <ul class="award-list">
          <li class="award-item">2023 — <strong>Valedictorian</strong>, <a href="https://www.cpr.cuhk.edu.hk/en/press/cuhk-holds-92nd-congregation-for-the-conferment-of-degrees/" target="_blank" rel="noopener noreferrer">CUHK Postgraduate Class of 2023</a></li>
          <li class="award-item">2023 — <strong><a href="https://2023.ieeeicassp.org/outstanding-reviewer-recognitions/" target="_blank" rel="noopener noreferrer">IEEE ICASSP Outstanding Reviewer</a></strong></li>
          <li class="award-item">2023 — <a href="https://interspeech2023.org/travel-grants/" target="_blank" rel="noopener noreferrer">ISCA INTERSPEECH Travel Grant</a></li>
          <li class="award-item">2019–23 — <a href="https://www.gs.cuhk.edu.hk/admissions/scholarships-fees/studentships" target="_blank" rel="noopener noreferrer">CUHK Postgraduate Studentship</a></li>
        </ul>
    </div>
  </details>
  <details id="award-group-undergraduate" class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">Undergraduate</span>
        <span class="award-card__meta">2015–2019 · 18 awards</span>
      </span>
    </summary>
    <div class="award-group__content">
        <ul class="award-list">
          <li class="award-item">2019 — <a href="https://www.hkxfoundation.org/aboutus" target="_blank" rel="noopener noreferrer">Finalist, Hong Kong X Foundation FYP+ Project</a></li>
          <li class="award-item">2019 — CUHK Academic Excellence Scholarship for Non-local Students</li>
          <li class="award-item">2019 — <strong><a href="https://www3.erg.cuhk.edu.hk/erg/Elite/Scholarship" target="_blank" rel="noopener noreferrer">CUHK ELITE Stream Student Scholarship</a></strong></li>
          <li class="award-item">2018-19 — <strong>Undergraduate Research Fellowship</strong>, sponsored by the Research Grants Council</li>
          <li class="award-item">2018 — Information Engineering Awards for Academic Exchange</li>
          <li class="award-item">2018 — <strong>CUHK Best Project Award for Undergraduate Research Summer Internship</strong></li>
          <li class="award-item">2018 — <a href="https://admission.cuhk.edu.hk/fees-financing-your-studies/scholarships/reaching-out-award/" target="_blank" rel="noopener noreferrer">HKSAR Government Reaching Out Award</a></li>
          <li class="award-item">2018 — CUHK S.H. Ho College Outstanding Student Scholarship</li>
          <li class="award-item">2017-18 — Arthur and Louise May Memorial Scholarship</li>
          <li class="award-item">2017 — Second Prize, Contemporary Undergraduate Mathematical Contest in Modeling (CUMCM)</li>
          <li class="award-item">2017 — CUHK S.H. Ho College Social Service Award</li>
          <li class="award-item">2017 — <strong><a href="https://admission.cuhk.edu.hk/fees-financing-your-studies/scholarships/talent-development-sch/" target="_blank" rel="noopener noreferrer">HKSAR Government Talent Development Scholarship (Innovation)</a></strong></li>
          <li class="award-item">2017 — <strong><a href="https://www.theiet.org/impact-society/awards-prizes-and-scholarships/iet-student-prizes" target="_blank" rel="noopener noreferrer">The IET Prize</a></strong>, the Institute of Engineering and Technology</li>
          <li class="award-item">2017 — CUHK S.H. Ho College Outstanding Student Scholarship</li>
          <li class="award-item">2016 — <strong><a href="https://www3.erg.cuhk.edu.hk/erg/Elite/Scholarship" target="_blank" rel="noopener noreferrer">CUHK ELITE Stream Student Scholarship</a></strong></li>
          <li class="award-item">2016 — CUHK S.H. Ho College Outstanding Student Scholarship</li>
          <li class="award-item">2015 — <strong><a href="https://www.csclf.org/" target="_blank" rel="noopener noreferrer">The Soong Ching Ling Foundation Zhiyuan Scholarship</a></strong></li>
          <li class="award-item">2015 — CUHK S.H. Ho College Outstanding Student Scholarship</li>
        </ul>
    </div>
  </details>
</div>

<h2 id="selected-talks">Selected Talks</h2>
<p class="award-section-meta">2022–2026 · 6 talks</p>
<div class="award-groups selected-talks">
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">2026</span>
        <span class="award-card__meta">1 talk</span>
      </span>
    </summary>
    <div class="award-group__content">
      <ul class="award-list">
        <li class="award-item"><strong>Reliable and Inclusive Speech and Language Technologies</strong>, <a href="https://www.psl.eu/en" target="_blank" rel="noopener noreferrer">Paris Sciences et Lettres University</a></li>
      </ul>
    </div>
  </details>
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">2025</span>
        <span class="award-card__meta">1 talk</span>
      </span>
    </summary>
    <div class="award-group__content">
      <ul class="award-list">
        <li class="award-item"><strong>Automatic Speech Recognition for Canadian Indigenous Languages</strong>, National Research Council Canada</li>
      </ul>
    </div>
  </details>
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">2024</span>
        <span class="award-card__meta">2 talks</span>
      </span>
    </summary>
    <div class="award-group__content">
      <ul class="award-list">
        <li class="award-item"><strong>Advancement in ASR Techniques to Support Indigenous Language Documentation</strong>, University of Toronto</li>
        <li class="award-item"><strong>Exploring Spectro-Temporal Features for Dysarthric and Elderly Speech Augmentation and Adaptation</strong>, National Research Council Canada</li>
      </ul>
    </div>
  </details>
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">2023</span>
        <span class="award-card__meta">1 talk</span>
      </span>
    </summary>
    <div class="award-group__content">
      <ul class="award-list">
        <li class="award-item"><strong>Towards Fair and Inclusive Speech Techniques for Dysarthric and Elderly Speakers</strong>, National Research Council Canada</li>
      </ul>
    </div>
  </details>
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">2022</span>
        <span class="award-card__meta">1 talk</span>
      </span>
    </summary>
    <div class="award-group__content">
      <ul class="award-list">
        <li class="award-item"><strong>Spectro-Temporal Deep Features for Disordered Speech Assessment and Recognition</strong>, presented as part of <a href="https://courses.grainger.illinois.edu/ece590sic/sp2022/index.html" target="_blank" rel="noopener noreferrer">ECE 590SIC: Audio, Speech and Language Processing</a>, University of Illinois Urbana-Champaign</li>
      </ul>
    </div>
  </details>
</div>

<h2 id="fundings">Fundings</h2>
<p><strong>Canadian federal funding eligibility.</strong> As an employee of the National Research Council Canada, my eligibility to apply as PI for Canadian federal research grants is limited under the <a href="https://ised-isde.canada.ca/site/science/en/interagency-research-funding/policies-and-guidelines/tri-agency-policy-use-funds-federal-government-employees-applying-granting-agency-programs" target="_blank" rel="noopener noreferrer">Tri-Agency policy</a> and depends on the program and proposed work. </p><p class="funding-collaboration-callout"><strong>Funding collaboration.</strong> I welcome funding collaborations worldwide—as co-PI/co-applicant where permitted, or as a collaborator. Please contact me at <a href="mailto:Mengzhe.Geng@nrc-cnrc.gc.ca">Mengzhe.Geng@nrc-cnrc.gc.ca</a>.</p>

<h2 id="teaching">Teaching</h2>
<div class="award-groups teaching-groups">
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">Institutional teaching and coordination</span>
        <span class="award-card__meta">The Chinese University of Hong Kong · 2018–2023</span>
      </span>
    </summary>
    <div class="award-group__content">
      <p>Teaching assistant and student coordinator at The Chinese University of Hong Kong (CUHK), 2018–2023.</p>
      <ul class="award-list">
        <li class="award-item"><a href="https://pg.com.cuhk.edu.hk/course-list/" target="_blank" rel="noopener noreferrer">COMM 5961/5962 — Topical Studies in New Media I/II</a></li>
        <li class="award-item"><a href="https://epin.cuhk.edu.hk/course/design-thinking-and-practice/index.html" target="_blank" rel="noopener noreferrer">EPIN 1020 — Design Thinking and Practice</a></li>
        <li class="award-item"><a href="https://seem.se.cuhk.edu.hk/programme-details/course-details/seem3490/" target="_blank" rel="noopener noreferrer">SEEM 3490 — Information Systems Management</a></li>
        <li class="award-item"><a href="https://seem.se.cuhk.edu.hk/programme-details/course-details/seem4540/" target="_blank" rel="noopener noreferrer">SEEM 4540 — Open Systems for E-Commerce</a></li>
        <li class="award-item"><a href="https://fintech.erg.cuhk.edu.hk/programme-information/master-science/master-science" target="_blank" rel="noopener noreferrer">FTEC 5910 — Financial Technology Project I</a></li>
        <li class="award-item"><a href="https://fintech.erg.cuhk.edu.hk/programme-information/master-science/master-science" target="_blank" rel="noopener noreferrer">FTEC 5920 — Financial Technology Project II</a></li>
        <li class="award-item"><a href="https://fintech.erg.cuhk.edu.hk/programme-information/master-science/master-science" target="_blank" rel="noopener noreferrer">FTEC 5540 — Financial Technology Internship</a></li>
      </ul>
    </div>
  </details>
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">Independent Instructor</span>
        <span class="award-card__meta">Mathematics · Computer Science · Data Science · Machine Learning · AI</span>
      </span>
    </summary>
    <div class="award-group__content">
      <p>I provide independent instruction across mathematics, computer science, data science, machine learning, and artificial intelligence. Examples include calculus, linear algebra, probability, discrete mathematics, data structures, and data mining, among many others. If you are looking for teaching services, please feel free to contact me at <a href="mailto:tim.geng.cuhk@gmail.com">tim.geng.cuhk@gmail.com</a>.</p>
    </div>
  </details>
  <details class="award-card award-group">
    <summary class="award-card__summary">
      <span class="award-card__summary-main">
        <span class="award-card__title" role="heading" aria-level="3">Guest lectures</span>
        <span class="award-card__meta">· 4 lectures</span>
      </span>
    </summary>
    <div class="award-group__content">
      <ul class="award-list">
        <li class="award-item">Nov 2026 — <strong>Carleton University</strong> · Topic to be confirmed</li>
        <li class="award-item">Nov 2026 — <strong>The Hong Kong Polytechnic University</strong> · Who Gets Heard? Building Inclusive Speech and Language Technologies</li>
        <li class="award-item">Nov 2026 — <strong>University of British Columbia</strong> · Topics to be determined</li>
        <li class="award-item">Nov 2026 — <strong>University of California, Berkeley</strong> · Topics to be determined</li>
      </ul>
    </div>
  </details>
</div>

<h2>Profiles</h2>
<p class="complete-publication-links">For the complete publication record, visit <a href="{{ site.author.googlescholar }}">Google Scholar</a> or browse the <a href="{{ '/publications/' | relative_url }}">Publications page</a>.</p>
