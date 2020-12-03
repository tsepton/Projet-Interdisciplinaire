const host = 'http://localhost:8080'
const stib = 'https://opendata-api.stib-mivb.be'
const token = '1b29a0b34badf9f5aeb006597fc7a76e'

async function shapefiles(file) {
  const response = await fetch(`${host}/shapefiles/${file}/`)
  const data = await response.json()
  if (response.ok) return data
  else throw new Error(data?.error)

}

async function vehiclePosition(lineIds) {
  let headers = { "Content-Type": "application/json" };
  headers["Authorization"] = `Bearer ${token}`;
  const response = await fetch(`${stib}/${lineIds.join(',')}`, { headers, })
  const data = await response.json()
  if (response.ok) return data
  else throw new Error(data?.error)
}

export { shapefiles, vehiclePosition }
