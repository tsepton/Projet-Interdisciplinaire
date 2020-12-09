const host = 'http://localhost:8080'
const stib = 'https://opendata-api.stib-mivb.be'
const token = '6be217669c174b42ceb7f0796aeea29f'

export async function shapefiles(file) {
  const response = await fetch(`${host}/shapefiles/${file}/`)
  const data = await response.json()
  if (response.ok) return data
  else throw new Error(data?.error)

}

export async function vehiclePosition(lineIds) {
  let headers = { "Content-Type": "application/json" };
  headers["Authorization"] = `Bearer ${token}`
  const response = await fetch(`${stib}/${lineIds.join(',')}`, { headers, })
  const data = await response.json()
  if (response.ok) return data
  else throw new Error(data?.error)
}

export async function stopsByLine(lineIds) {
  let headers = { "Content-Type": "application/json" };
  headers["Authorization"] = `Bearer ${token}`
  const response = await fetch(`${stib}`
    + "/NetworkDescription/1.0/PointByLine/"
    + `${lineIds.join(',')}`, { headers, })
  const data = await response.json()
  if (response.ok) return data
  else throw new Error(data?.error)
}

export async function delay(line, stop, direction) {
  const response = await fetch(`${host}/delay`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ stop, line, direction })
  })
  const data = await response.json()
  if (response.ok) return data
  else throw new Error(data?.error)
}
