export default function App() {
  const premiumLogo = "/logo-main.png";
  const heroImage =
    "https://images.unsplash.com/photo-1473968512647-3e447244af8f?q=80&w=2200&auto=format&fit=crop";

  const services = [
    {
      title: "Insurance Claim Support Photos",
      description:
        "Clear aerial imagery for adjusters documenting roof and exterior conditions for claims, supplements, and file review.",
    },
    {
      title: "Roof Photo Documentation",
      description:
        "Structured photo sets showing visible roof condition, elevations, and exterior areas that need attention or follow up.",
    },
    {
      title: "Real Estate Listing Photos",
      description:
        "Professional aerial visuals that help present property condition, improve listing presentation, and reduce surprises during the sales process.",
    },
    {
      title: "Homeowner Roof Photos",
      description:
        "Useful documentation for homeowners who want current roof imagery for insurance, storm prep, or post storm records.",
    },
  ];

  const process = [
    {
      step: "01",
      title: "Send the property details",
      text: "Share the address, property type, and any areas you want documented.",
    },
    {
      step: "02",
      title: "We capture the site",
      text: "A focused flight is performed to gather clean, usable aerial visuals.",
    },
    {
      step: "03",
      title: "Receive organized images",
      text: "You get polished deliverables that are easy to review, save, and share.",
    },
  ];

  const highlights = [
    "FAA Part 107 Certified",
    "Firefighter Owned & Operated",
    "24 Hour Turnaround Available",
    "Palm Beach & Broward Based",
  ];

  const clients = [
    {
      title: "Adjusters",
      description:
        "Support for private and public adjusters who need clear, structured imagery for documentation, review, and claim support.",
    },
    {
      title: "Realtors",
      description:
        "Aerial visuals that help properties present better online and help buyers understand layout and exterior condition.",
    },
    {
      title: "Homeowners",
      description:
        "Roof documentation for insurance, peace of mind, and before and after storm condition records.",
    },
  ];

  const deliverables = [
    "High resolution aerial property images",
    "Full roof overview angles",
    "Focused exterior condition photos",
    "Organized image delivery for easier review",
    "Claim and listing friendly photo sets",
    "Fast turnaround available",
  ];

  const audienceSplit = [
    {
      title: "For Adjusters",
      points: [
        "Faster visual documentation for claims",
        "Useful support for supplements and file review",
        "Clear roof and exterior condition imagery",
      ],
    },
    {
      title: "For Realtors",
      points: [
        "Stronger listing presentation",
        "Better buyer understanding of the property",
        "Reduced surprises during the sales process",
      ],
    },
  ];

  const trustItems = [
    "FAA Part 107 Certified Remote Pilot",
    "Serving South Florida",
    "Professional communication and organized delivery",
    "Built for adjusters, realtors, and homeowners",
  ];

  const pricing = [
    {
      title: "Standard Property Shoot",
      price: "Starting at $150",
      text: "Ideal for standard residential aerial documentation and listing support.",
    },
    {
      title: "Complex or Larger Roofs",
      price: "Custom Quote",
      text: "For larger homes, complex rooflines, or jobs needing added image coverage.",
    },
    {
      title: "Rush Turnaround",
      price: "Available",
      text: "Same day or priority scheduling may be available depending on workload and location.",
    },
  ];

  const faqs = [
    {
      q: "How fast do I receive the photos?",
      a: "Turnaround depends on the job, but fast delivery is available and rush scheduling may be possible in many cases.",
    },
    {
      q: "Can these photos be used for insurance documentation?",
      a: "Yes. The service is designed to provide clean aerial imagery that supports property documentation and claim related review.",
    },
    {
      q: "Do I need to be on site?",
      a: "Not always. That depends on access, property conditions, and the type of documentation needed.",
    },
    {
      q: "Do you go on the roof?",
      a: "The focus is aerial documentation. The goal is to capture useful visuals without unnecessary climbing exposure.",
    },
  ];

  return (
    <div className="min-h-screen bg-[#07090c] text-white">
      <section id="home" className="relative isolate overflow-hidden border-b border-white/10">
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: `url(${heroImage})` }}
        />
        <div className="absolute inset-0 bg-[linear-gradient(180deg,rgba(4,7,11,0.48)_0%,rgba(4,7,11,0.76)_35%,rgba(4,7,11,0.94)_100%)]" />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(220,38,38,0.18),transparent_26%)]" />

        <div className="relative mx-auto max-w-7xl px-6 pb-24 pt-6 md:px-10 md:pb-32">
          <header className="flex flex-col gap-6 rounded-[2rem] border border-white/10 bg-black/25 px-5 py-4 backdrop-blur md:flex-row md:items-center md:justify-between">
            <div className="flex items-center gap-3">
              <img
  src={premiumLogo}
  alt="Redline Aerial logo"
  className="h-14 md:h-16 object-contain brightness-125 contrast-125"
/>
              <div>
                <div className="text-lg font-black uppercase tracking-[0.2em] text-white">Redline Aerial</div>
                
              </div>
            </div>

            <nav className="flex flex-wrap gap-6 text-sm font-semibold uppercase tracking-[0.22em] text-white/85 md:text-base">
              <a href="#home" className="transition hover:text-red-300">Home</a>
              <a href="#services" className="transition hover:text-red-300">Services</a>
              <a href="#about" className="transition hover:text-red-300">About</a>
              <a href="#contact" className="transition hover:text-red-300">Contact</a>
            </nav>

            <div className="text-right text-sm leading-6 text-white/75">
              <div>FAA Part 107 Certified</div>
              <div>Serving adjusters, realtors, and homeowners</div>
            </div>
          </header>

          <div className="grid gap-12 pt-14 lg:grid-cols-[1.05fr_0.95fr] lg:items-end lg:pt-20">
            <div className="max-w-3xl">
              <div className="inline-flex items-center rounded-full border border-red-500/30 bg-red-500/10 px-4 py-2 text-xs font-semibold uppercase tracking-[0.28em] text-red-200 backdrop-blur">
                Premium aerial documentation
              </div>

              <h1 className="mt-8 text-5xl font-black uppercase leading-[0.95] tracking-tight text-white drop-shadow-[0_6px_24px_rgba(0,0,0,0.5)] md:text-7xl">
                FAST DRONE PHOTOS.
                <br />
                FOR CLAIMS & LISTINGS.
              </h1>

              <p className="mt-6 max-w-2xl text-lg leading-8 text-white/78 md:text-xl">
               Serving Palm Beach, Broward, and South Florida with fast drone photos for claims, roofs, and listings.
              </p>

              <div className="mt-10 flex flex-col gap-4 sm:flex-row">
                <a
                  href="#contact"
                  className="rounded-2xl bg-red-600 px-7 py-4 text-center text-sm font-black uppercase tracking-[0.2em] text-white shadow-[0_18px_50px_rgba(220,38,38,0.35)] hover:bg-red-500 hover:scale-105 transition-all duration-300"
                >
                  Request Quote
                </a>
                <a
                  href="#services"
                  className="rounded-2xl border border-white/15 bg-white/5 px-7 py-4 text-center text-sm font-bold uppercase tracking-[0.2em] text-white backdrop-blur hover:bg-white/10 opacity-80 hover:opacity-100 transition"
                >
                  OUR SERVICES
                </a>
              </div>

              <div className="mt-12 grid gap-4 sm:grid-cols-2">
                {highlights.map((item) => (
                  <div
                    key={item}
                    className="rounded-2xl border border-white/10 bg-white/5 px-5 py-4 text-sm font-medium text-white/82 backdrop-blur"
                  >
                    {item}
                  </div>
                ))}
              </div>
            </div>

            <div className="rounded-[2rem] border border-white/10 bg-black/25 p-6 shadow-2xl backdrop-blur-md lg:ml-8">
              <div className="rounded-[1.5rem] border border-white/10 bg-white/5 p-7">
                <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Core focus</p>
                <h2 className="mt-4 text-3xl font-bold text-white">High trust visuals for property decisions</h2>
                <p className="mt-4 leading-8 text-white/72">
                  Redline Aerial is built around clean presentation, usable documentation, and a premium client experience from first contact to final delivery.
                </p>

                <div className="mt-8 space-y-4">
                  <div className="rounded-2xl border border-white/10 bg-black/25 px-5 py-4 text-white/80">Claim documentation support</div>
                  <div className="rounded-2xl border border-white/10 bg-black/25 px-5 py-4 text-white/80">Roof and exterior condition imagery</div>
                  <div className="rounded-2xl border border-white/10 bg-black/25 px-5 py-4 text-white/80">Listing visuals for real estate teams</div>
                  <div className="rounded-2xl border border-white/10 bg-black/25 px-5 py-4 text-white/80">Organized delivery for easier review</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="services" className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#0a0c10_0%,#10131a_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(220,38,38,0.12),transparent_36%)]" />
        <div className="relative mx-auto max-w-7xl px-6 py-24 md:px-10">
          <div className="mx-auto max-w-3xl text-center">
            <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Services</p>
            <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
              Professional aerial support for property related decisions.
            </h2>
            <p className="mt-5 text-lg leading-8 text-white/72">
              Every service is designed to give the client clean visuals, clearer understanding, and a more professional presentation.
            </p>
          </div>

          <div className="mt-14 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
            {services.map((service) => (
              <div
                key={service.title}
                className="group rounded-[1.8rem] border border-white/10 bg-white/5 p-7 shadow-xl backdrop-blur transition duration-300 hover:-translate-y-1 hover:border-red-400/40 hover:bg-white/8"
              >
                <div className="mb-6 h-1.5 w-16 rounded-full bg-red-500 transition group-hover:w-24" />
                <h3 className="text-2xl font-semibold text-white">{service.title}</h3>
                <p className="mt-4 leading-8 text-white/72">{service.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="about" className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#10131a_0%,#0a0c10_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_right,rgba(220,38,38,0.12),transparent_34%)]" />
        <div className="relative mx-auto grid max-w-7xl gap-10 px-6 py-24 md:px-10 lg:grid-cols-[1fr_0.92fr]">
          <div>
            <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">About</p>
            <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
              Built around clarity, speed, and presentation.
            </h2>
            <p className="mt-5 max-w-2xl text-lg leading-8 text-white/72">
              Clients do not need flashy footage. They need visuals that help them review a property faster, communicate more clearly, and move the job forward with confidence.
            </p>

            <div className="mt-10 grid gap-4 sm:grid-cols-2">
              {clients.map((client, index) => (
                <div
                  key={client.title}
                  className={`rounded-[1.6rem] border border-white/10 bg-white/5 p-6 backdrop-blur ${index === 2 ? "sm:col-span-2" : ""}`}
                >
                  <h3 className="text-2xl font-semibold text-white">{client.title}</h3>
                  <p className="mt-3 leading-8 text-white/72">{client.description}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-[2rem] border border-white/10 bg-white/5 p-8 shadow-2xl backdrop-blur-md">
            <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Process</p>
            <h3 className="mt-4 text-3xl font-bold text-white">Simple from request to delivery</h3>
            <div className="mt-8 space-y-5">
              {process.map((item) => (
                <div key={item.step} className="flex gap-4 rounded-[1.5rem] border border-white/10 bg-black/20 p-5">
                  <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-red-600 text-sm font-black tracking-[0.18em] text-white">
                    {item.step}
                  </div>
                  <div>
                    <h4 className="text-lg font-semibold text-white">{item.title}</h4>
                    <p className="mt-2 leading-7 text-white/70">{item.text}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#0b0d12_0%,#10141c_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_left,rgba(220,38,38,0.12),transparent_30%)]" />
        <div className="relative mx-auto max-w-7xl px-6 py-24 md:px-10">
          <div className="mx-auto max-w-3xl text-center">
            <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">What You Receive</p>
            <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
              Deliverables built for real world use.
            </h2>
            <p className="mt-5 text-lg leading-8 text-white/72">
              The goal is not random drone footage. It is clean, useful imagery that helps the client review the property, communicate clearly, and move forward faster.
            </p>
          </div>

          <div className="mt-14 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {deliverables.map((item) => (
              <div key={item} className="rounded-[1.5rem] border border-white/10 bg-white/5 px-6 py-5 text-white/82 backdrop-blur">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#10141c_0%,#0b0d12_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(220,38,38,0.10),transparent_34%)]" />
        <div className="relative mx-auto max-w-7xl px-6 py-24 md:px-10">
          <div className="grid gap-8 lg:grid-cols-2">
            {audienceSplit.map((group) => (
              <div key={group.title} className="rounded-[2rem] border border-white/10 bg-white/5 p-8 shadow-2xl backdrop-blur-md">
                <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Audience Focus</p>
                <h2 className="mt-4 text-3xl font-bold text-white">{group.title}</h2>
                <div className="mt-8 space-y-4">
                  {group.points.map((point) => (
                    <div key={point} className="rounded-2xl border border-white/10 bg-black/20 px-5 py-4 text-white/80">
                      {point}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#0b0d12_0%,#10141c_100%)]">
        <div className="relative mx-auto max-w-7xl px-6 py-20 md:px-10">
          <div className="grid gap-4 rounded-[2rem] border border-white/10 bg-white/5 p-6 shadow-2xl backdrop-blur md:grid-cols-2 xl:grid-cols-4">
            {trustItems.map((item) => (
              <div key={item} className="rounded-2xl border border-white/10 bg-black/20 px-5 py-4 text-center text-sm font-semibold uppercase tracking-[0.16em] text-white/82">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#10141c_0%,#0b0d12_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_right,rgba(220,38,38,0.10),transparent_34%)]" />
        <div className="relative mx-auto max-w-7xl px-6 py-24 md:px-10">
          <div className="mx-auto max-w-3xl text-center">
            <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Pricing</p>
            <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
              Simple pricing guidance.
            </h2>
            <p className="mt-5 text-lg leading-8 text-white/72">
              Clear starting points help clients understand the service quickly. Final pricing can still vary based on property size, complexity, and turnaround needs.
            </p>
          </div>

          <div className="mt-14 grid gap-6 md:grid-cols-3">
            {pricing.map((item) => (
              <div key={item.title} className="rounded-[1.8rem] border border-white/10 bg-white/5 p-7 shadow-xl backdrop-blur-md">
                <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Option</p>
                <h3 className="mt-4 text-2xl font-semibold text-white">{item.title}</h3>
                <div className="mt-4 text-3xl font-black text-white">{item.price}</div>
                <p className="mt-5 leading-8 text-white/72">{item.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#0b0d12_0%,#10141c_100%)]">
        <div className="relative mx-auto max-w-7xl px-6 py-24 md:px-10">
          <div className="mx-auto max-w-3xl text-center">
            <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Frequently Asked Questions</p>
            <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
              Common questions, answered clearly.
            </h2>
          </div>

          <div className="mx-auto mt-14 max-w-4xl space-y-5">
            {faqs.map((item) => (
              <div key={item.q} className="rounded-[1.6rem] border border-white/10 bg-white/5 p-6 backdrop-blur-md">
                <h3 className="text-xl font-semibold text-white">{item.q}</h3>
                <p className="mt-3 leading-8 text-white/72">{item.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="relative overflow-hidden border-b border-white/10 bg-[linear-gradient(180deg,#10141c_0%,#090b10_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(220,38,38,0.16),transparent_30%)]" />
        <div className="relative mx-auto max-w-6xl px-6 py-24 text-center md:px-10">
          <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Final Call To Action</p>
          <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-6xl">
            Clear visuals. Faster decisions. Less back and forth.
          </h2>
          <p className="mx-auto mt-6 max-w-3xl text-lg leading-8 text-white/72">
            Redline Aerial helps adjusters, realtors, and homeowners get professional aerial photography that is easier to use, easier to review, and easier to act on.
          </p>
          <div className="mt-10 flex flex-col justify-center gap-4 sm:flex-row">
            <a
              href="#contact"
              className="rounded-2xl bg-red-600 px-8 py-4 text-center text-sm font-black uppercase tracking-[0.2em] text-white shadow-[0_18px_50px_rgba(220,38,38,0.35)] transition hover:bg-red-500"
            >
              Request Inspection Photos
            </a>
            <a
              href="mailto:redlineaerialpb@gmail.com"
              className="rounded-2xl border border-white/15 bg-white/5 px-8 py-4 text-center text-sm font-bold uppercase tracking-[0.2em] text-white backdrop-blur transition hover:bg-white/10"
            >
              Email For Availability
            </a>
          </div>
        </div>
      </section>

      <section id="contact" className="relative overflow-hidden bg-[linear-gradient(180deg,#0a0c10_0%,#08090c_100%)]">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(220,38,38,0.16),transparent_30%)]" />
        <div className="relative mx-auto max-w-7xl px-6 py-24 md:px-10">
          <div className="grid gap-8 rounded-[2rem] border border-white/10 bg-white/5 p-8 shadow-2xl backdrop-blur-md lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
            <div>
              <p className="text-xs font-semibold uppercase tracking-[0.28em] text-red-300">Quick Quote</p>
              <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
                Need Fast Drone Photos For A Claim, Listing, Or Roof Record?
              </h2>
              <p className="mt-5 max-w-2xl text-lg leading-8 text-white/72">
                Fast professional drone photos for claims, roof records, listings, and property documentation throughout South Florida.
              </p>
            </div>

            <div className="rounded-[1.8rem] border border-white/10 bg-black/25 p-6">
              <div className="space-y-4 text-white/82">
                <div className="rounded-2xl border border-white/10 bg-white/5 px-5 py-4">redlineaerialpb@gmail.com</div>
                <div className="rounded-2xl border border-white/10 bg-white/5 px-5 py-4">FAA Part 107 Certified Operator</div>
                <div className="rounded-2xl border border-white/10 bg-white/5 px-5 py-4">Serving Adjusters, Realtors & Homeowners</div>
              </div>

              <a
                href="mailto:redlineaerialpb@gmail.com"
                className="mt-6 block rounded-2xl bg-red-600 px-6 py-4 text-center text-sm font-black uppercase tracking-[0.22em] text-white shadow-[0_18px_50px_rgba(220,38,38,0.30)] transition hover:bg-red-500"
              >
                GET FAST QUOTE
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
