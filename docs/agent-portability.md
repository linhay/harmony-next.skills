# Agent Portability

`harmony-next/SKILL.md` is the source of truth. Host-specific instructions should point agents at that skill directory instead of copying the full rule text.

## Supported Paths

| Host | Current path | Notes |
| --- | --- | --- |
| skills.sh / generic skills CLI | `npx skills add linhay/harmony-next.skills` | Recommended default. Installs the repository's single `harmony-next` skill. |
| Gemini CLI | `gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user` | Loads the skill directory directly. |
| Claude Code | `npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy` | Use `--copy` for non-interactive global installs. |
| Claude.ai | release artifact `harmony-next.skill.zip` | Upload the packaged skill artifact when a file upload flow is needed. |
| Codex | `npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy` | Current distribution is a skill install, not a Codex plugin. |
| Codex manual install | `$REPO_ROOT/.agents/skills/harmony-next`, `$HOME/.agents/skills/harmony-next`, or `/etc/codex/skills/harmony-next` | Copy or symlink the `harmony-next/` directory. |
| DeepSeek Harness (DSH) | `dsh plugin --profile demo add github:linhay/harmony-next.skills` | Official DSH profile bundle; manual filesystem roots remain a fallback. |
| Generic project instructions | repository `AGENTS.md` plus `harmony-next/SKILL.md` | `AGENTS.md` stays small; the skill contains the HarmonyOS routing rules. |

## DeepSeek Harness (DSH)

This repository is distributed as the official DSH profile bundle `dsh-harmony-next`. The bundle keeps `harmony-next/SKILL.md` as the source of truth and mounts a small provider that exposes the bundled Skill and its relative `references/` and `scripts/` resources.

The repository root contains the bundle contract:

```text
package.json       # dsh.bundle.patch -> ./cordis.patch.yml
cordis.patch.yml   # inserts the dsh-harmony-next provider
index.js           # registers harmony-next in ctx.skills
harmony-next/      # the existing Skill and offline resources
```

The current DSH `dsh-skill-filesystem` provider still discovers directory bundles shaped like `<skill-root>/<name>/SKILL.md`. The same `harmony-next/` directory remains compatible with that provider for manual installs; the profile bundle is the recommended package installation path.

### Official profile-bundle installation

Install from GitHub:

```bash
dsh plugin --profile demo add github:linhay/harmony-next.skills
```

Or install a local checkout:

```bash
dsh plugin --profile demo add /path/to/harmony-next.skills
```

The first command adds the package dependency and, because its manifest declares `dsh.bundle`, adds `dsh-harmony-next` to the profile's bundle layer. Inspect the composed configuration without starting a model session:

```bash
dsh --profile demo --dump-config
```

This bundle registers only the `harmony-next` Skill and its offline resources. It does not mount MCP servers, model tools, apps, or unrelated Cordis services.

### Discovery roots

DSH checks these roots in precedence order:

| Rank | Source | Root |
| ---: | --- | --- |
| 100 | project-dsh | `<projectRoot>/.dsh/skills` |
| 200 | project-agents | `<projectRoot>/.agents/skills` |
| 300 | custom | configured `customSkillDirs` |
| 400 | user-dsh | `$DSH_HOME/skills` (default `~/.dsh/skills`) |
| 500 | user-agents | `$DSH_AGENTS_HOME/skills` (default `~/.agents/skills`) |

### Filesystem-skill fallback

For a project-local or user-global filesystem Skill without a profile bundle, `DSH_SOURCE` must point to a checkout of this repository. Copy the contents of `harmony-next/` into the final skill directory so the file lands exactly at `harmony-next/SKILL.md`:

```bash
DSH_SOURCE=/path/to/harmony-next.skills

# Project-local
mkdir -p .dsh/skills/harmony-next
cp -R "$DSH_SOURCE/harmony-next/." .dsh/skills/harmony-next/

# User-level
mkdir -p "$HOME/.dsh/skills/harmony-next"
cp -R "$DSH_SOURCE/harmony-next/." "$HOME/.dsh/skills/harmony-next/"
```

If the source is not checked out yet, clone it first and set `DSH_SOURCE` to the clone directory. DSH can also read the same directory through `.agents/skills` or `$DSH_AGENTS_HOME/skills`.

### Verification

After bundle installation, run `dsh --profile demo --dump-config` and start DSH with that profile. The `harmony-next` skill should appear in the session skill catalog and in the `/` skill picker. The validation run also calls the DSH Web API's `session.create` and `skill.list` endpoints against an isolated profile.

Verified on 2026-08-15 with `@deepseek-ai/dsh@0.1.0-rc.6`:

- profile bundle installed from the local checkout into an isolated `web` profile: passed;
- project-level `.dsh/skills/harmony-next/SKILL.md`: passed;
- user-level `$DSH_HOME/skills/harmony-next/SKILL.md`: passed;
- bundle catalog returns `name: harmony-next`, the full description, and `modelInvocable: true`.

The smoke test verifies bundle installation, provider registration, discovery, frontmatter projection, and relative resource-base metadata without making a model request. It does not claim to verify provider credentials, model execution, or every DSH runtime version.

### Runtime plugin boundary

Do not install this repository as the removed `.dsh-plugin` format. Current DSH external extensions use profile bundles with a `dsh.bundle.patch` manifest. This bundle intentionally contributes only a Skill provider; it does not add MCP, tools, apps, or other runtime features.

## Adapter Rule

Keep adapters thin:

- Put behavior and routing in `harmony-next/SKILL.md`.
- Put user-facing installation instructions in `README.md` and `README_en.md`.
- Put host support notes here.
- Use `harmony-next/scripts/check_packaging_docs.py` to catch version, command, and path drift.

## Out Of Scope

This repository is a reference and automation skill pack, not an always-on behavior mode. Do not add lifecycle hooks, status lines, mode trackers, or per-host copied rule files unless a concrete host integration requires them.
