import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const PROVIDER_NAME = 'dsh-harmony-next'
const SKILL_NAME = 'harmony-next'
const BUNDLED_SKILL_RANK = 600
const SKILL_ROOT = fileURLToPath(new URL('./harmony-next/', import.meta.url))
const SKILL_PATH = fileURLToPath(new URL('./harmony-next/SKILL.md', import.meta.url))
const FRONTMATTER_PATTERN = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/

function booleanValue(value, fallback, label) {
  if (value === undefined) return fallback
  if (typeof value === 'boolean') return value
  const normalized = String(value).trim().toLowerCase()
  if (['true', 'yes', 'on', '1'].includes(normalized)) return true
  if (['false', 'no', 'off', '0'].includes(normalized)) return false
  throw new TypeError(`${label} must be a boolean`)
}

function scalarValue(value) {
  const trimmed = value.trim()
  if (trimmed === '') return ''
  if (trimmed.startsWith('"') && trimmed.endsWith('"')) {
    return JSON.parse(trimmed)
  }
  if (trimmed.startsWith("'") && trimmed.endsWith("'")) {
    return trimmed.slice(1, -1).replaceAll("''", "'")
  }
  if (trimmed === 'true' || trimmed === 'false') return trimmed === 'true'
  if (trimmed === 'null' || trimmed === '~') return null
  return trimmed
}

/**
 * Parse the small, stable frontmatter shape owned by this package.
 * The authoritative DSH filesystem provider remains responsible for general
 * YAML skill parsing; this packaged provider only needs this repository's
 * name, description, invocation flags, metadata, and optional whenToUse.
 */
function parseFrontmatter(source) {
  const values = {}
  let section
  for (const line of source.split(/\r?\n/)) {
    if (line.trim() === '' || line.trimStart().startsWith('#')) continue
    const topLevel = /^(?<key>[A-Za-z0-9_-]+):\s*(?<value>.*)$/.exec(line)
    if (topLevel !== null) {
      const key = topLevel.groups.key
      const value = topLevel.groups.value
      if (value === '') {
        values[key] = {}
        section = key
      } else {
        values[key] = scalarValue(value)
        section = undefined
      }
      continue
    }

    const nested = /^  (?<key>[A-Za-z0-9_-]+):\s*(?<value>.*)$/.exec(line)
    if (nested !== null && section !== undefined && typeof values[section] === 'object' && values[section] !== null) {
      values[section][nested.groups.key] = scalarValue(nested.groups.value)
      continue
    }
    throw new Error(`unsupported frontmatter line: ${line}`)
  }
  return values
}

function readSkill() {
  const source = readFileSync(SKILL_PATH, 'utf8')
  const match = FRONTMATTER_PATTERN.exec(source)
  if (match === null) throw new Error(`${SKILL_PATH} is missing YAML frontmatter`)

  const frontmatter = parseFrontmatter(match[1])
  if (frontmatter === null || typeof frontmatter !== 'object' || Array.isArray(frontmatter)) {
    throw new TypeError(`${SKILL_PATH} frontmatter must be a YAML object`)
  }

  const name = frontmatter.name
  const description = frontmatter.description
  if (name !== SKILL_NAME) throw new Error(`expected skill name ${SKILL_NAME}, got ${String(name)}`)
  if (typeof description !== 'string' || description.trim() === '') {
    throw new Error(`${SKILL_PATH} requires a non-empty description`)
  }

  const metadata = frontmatter.metadata
  const definition = {
    name: SKILL_NAME,
    description,
    invocation: {
      modelInvocable: !booleanValue(frontmatter['disable-model-invocation'], false, 'disable-model-invocation'),
      userInvocable: booleanValue(frontmatter['user-invocable'], true, 'user-invocable'),
    },
    source: 'bundled',
    provider: PROVIDER_NAME,
    resourceBase: { kind: 'directory', path: SKILL_ROOT },
    path: SKILL_PATH,
    content: source.slice(match[0].length),
    ...(typeof frontmatter.whenToUse === 'string' ? { whenToUse: frontmatter.whenToUse } : {}),
    ...(metadata !== null && typeof metadata === 'object' && !Array.isArray(metadata) ? { metadata } : {}),
  }
  return definition
}

const definition = Object.freeze(readSkill())
const candidate = Object.freeze({
  ...definition,
  rank: BUNDLED_SKILL_RANK,
  locator: SKILL_PATH,
})

const provider = {
  name: PROVIDER_NAME,
  async list() {
    return [candidate]
  },
  async get() {
    return { ...definition }
  },
}

export const name = PROVIDER_NAME
export const inject = ['skills']

export function apply(ctx) {
  ctx.skills.registerProvider(() => provider)
}
