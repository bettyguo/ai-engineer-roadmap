import type { Curator, Peer } from "../types";

interface Props {
  peers: Peer[];
  curator: Curator;
  repo: string;
}

export function PeerFooter({ peers, curator, repo }: Props) {
  return (
    <footer className="border-t border-ink-900/60 bg-ink-950/95 mt-auto">
      <div className="px-5 py-6 grid gap-6 md:grid-cols-2">
        <div>
          <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-100/55 mb-3">
            The constellation
          </div>
          <ul className="space-y-3">
            {peers.map((p) => (
              <li key={p.id}>
                <a
                  href={p.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block group hover:bg-ink-900/40 rounded-sm p-2 -mx-2"
                >
                  <div className="font-serif text-base group-hover:underline">{p.title}</div>
                  <div className="text-xs text-ink-100/75 leading-relaxed mt-0.5">{p.blurb}</div>
                  <div className="text-[10px] uppercase tracking-wider text-ink-100/55 mt-1">
                    {p.role} · open when: {p.openWhen}
                  </div>
                </a>
              </li>
            ))}
          </ul>
        </div>
        <div className="md:text-right space-y-3">
          <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-100/55">
            Curator
          </div>
          <div className="text-sm text-ink-50/90 leading-relaxed">
            <div className="font-serif text-base">{curator.name}</div>
            <div className="text-ink-100/80">{curator.affiliation}</div>
            {curator.advisor && (
              <div className="text-ink-100/80">Advisor: {curator.advisor}</div>
            )}
            <div className="mt-1 text-xs">
              <a
                href={`https://github.com/${curator.github}`}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:underline mr-3"
              >
                @{curator.github}
              </a>
              <a
                href={`https://orcid.org/${curator.orcid}`}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:underline"
              >
                ORCID {curator.orcid}
              </a>
            </div>
            <div className="text-xs text-ink-100/55 mt-2">
              <a href={repo} target="_blank" rel="noopener noreferrer" className="hover:underline">
                source on github
              </a>{" "}
              · content CC BY 4.0 · code MIT
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
