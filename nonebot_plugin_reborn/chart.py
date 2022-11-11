CHART_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@4.9.0/dist/echarts.min.js"></script>
    <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@4.9.0/map/js/world.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0
        }

        html,
        body {
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        #main {
            width: 100%;
            height: 100%;
            margin: 0px auto;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <div id="main"></div>
    <script type="text/javascript">
        const chart = echarts.init(document.getElementById('main'));
        const zoom = {{ZOOM}};
        const name = '{{NAME_EN}}';
        const coordinate = [{{LONGTITUDE}}, {{LATITUDE}}];
        const option = {
            backgroundColor: '#E8E8E8',
            geo: {
                map: 'world',
                roam: true,
                zoom: zoom,
                center: coordinate,
                silent: true,
                itemStyle: {
                    normal: {
                        areaColor: '#CFCFCF',
                        borderColor: '#111'
                    }
                }
            },
            visualMap: {
                min: 0,
                max: 1,
                inRange: {
                    color: ['#CFCFCF', '#2a333d']
                },
                show: false
            },
            series: [
                {
                    type: 'map',
                    geoIndex: 0,
                    data: [{ name: name, value: 1 }]
                }
            ]
        };
        chart.setOption(option);
    </script>
</body>
</html>
'''

def get_chart_html(name_en, longtitude, latitude, zoom=2.5):
    html = CHART_HTML.replace('{{NAME_EN}}', name_en).replace('{{LONGTITUDE}}', str(longtitude)).replace('{{LATITUDE}}', str(latitude)).replace('{{ZOOM}}', str(zoom))
    return html