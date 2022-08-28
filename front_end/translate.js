const fs = require('fs')

data = fs.readFileSync('./translate.txt','utf-8')
const t_dict = {}
for(const item of data.split(/\r?\n/)){
    const split = item.split('\t')
    if (split.length < 2) continue
    t_dict[split[0]] = split[1]
}
fs.writeFileSync('./translated.json', JSON.stringify(t_dict),'utf-8')