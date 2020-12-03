const host = 'http://localhost:8080'

async function shapefiles(file) {
  const response = await fetch(`${host}/shapefiles/${file}/`)
  const data = await response.json()
  if (response.ok) {
    return data
  } else {
    throw new Error(data?.error)
  }
}

export {shapefiles}
