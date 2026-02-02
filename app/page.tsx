import { Geist, Geist_Mono } from "next/font/google"

const geistSans = Geist({
  subsets: ["latin"],
  variable: "--font-geist-sans",
})

const geistMono = Geist_Mono({
  subsets: ["latin"],
  variable: "--font-geist-mono",
})

export default function Home() {
  return (
    <main
      className={`${geistSans.variable} ${geistMono.variable} min-h-screen bg-background text-foreground`}
    >
      <div className="container mx-auto px-6 py-16">
        <header className="mb-16">
          <h1 className="font-sans text-5xl font-bold tracking-tight mb-4">
            Geist Font
          </h1>
          <p className="font-sans text-xl text-muted-foreground max-w-2xl">
            A typeface designed for legibility and simplicity. Made by Vercel in
            collaboration with Basement Studio.
          </p>
        </header>

        <section className="mb-16">
          <h2 className="font-sans text-2xl font-semibold mb-8">Geist Sans</h2>
          <div className="space-y-6">
            {[100, 200, 300, 400, 500, 600, 700, 800, 900].map((weight) => (
              <div key={weight} className="flex items-baseline gap-6">
                <span className="font-mono text-sm text-muted-foreground w-16">
                  {weight}
                </span>
                <p
                  className="font-sans text-3xl"
                  style={{ fontWeight: weight }}
                >
                  The quick brown fox jumps over the lazy dog
                </p>
              </div>
            ))}
          </div>
        </section>

        <section className="mb-16">
          <h2 className="font-sans text-2xl font-semibold mb-8">Geist Mono</h2>
          <div className="space-y-6">
            {[100, 200, 300, 400, 500, 600, 700, 800, 900].map((weight) => (
              <div key={weight} className="flex items-baseline gap-6">
                <span className="font-mono text-sm text-muted-foreground w-16">
                  {weight}
                </span>
                <p
                  className="font-mono text-3xl"
                  style={{ fontWeight: weight }}
                >
                  {"const greeting = \"Hello, World!\";"}
                </p>
              </div>
            ))}
          </div>
        </section>

        <section className="mb-16">
          <h2 className="font-sans text-2xl font-semibold mb-8">
            Character Set
          </h2>
          <div className="font-sans text-4xl leading-relaxed tracking-wide">
            ABCDEFGHIJKLMNOPQRSTUVWXYZ
            <br />
            abcdefghijklmnopqrstuvwxyz
            <br />
            0123456789
            <br />
            {"!@#$%^&*()_+-=[]{}|;':\",./<>?"}
          </div>
        </section>

        <footer className="pt-8 border-t border-border">
          <p className="font-sans text-sm text-muted-foreground">
            Open source typeface by Vercel. Licensed under the SIL Open Font
            License.
          </p>
        </footer>
      </div>
    </main>
  )
}
