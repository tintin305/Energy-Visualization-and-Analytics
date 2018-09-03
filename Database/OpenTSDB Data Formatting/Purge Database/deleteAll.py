import os
import requests

def loadMetrics():
    # csvPath = os.path.dirname(__file__)
    # os.chdir(csvPath)
    f= open('Metrics.txt', 'r')
    metrics = f.readlines()
    return metrics

def generateURL(metric):
    # metricsParams = { 'host': 'localhost', 'port': 4242}
    metricsParams = {'aggregator' : 'avg', 'downsample' : '1m-sum', 'rate': 'false', 'metric': 'WITS_EC_Matrix_Main_Incomer_kWh', 'tagKey': 'DataLoggerName', 'tagValue': 'WITS_EC_Matrix_Main_Incomer_kWh', 'host': 'localhost', 'port': 4242, 'ms': 'false', 'arrays': 'true', 'tsuids': 'false', 'annotations': 'none', 'startDate': '10y-ago', 'endDate': '1d-ago'}

    aggregator = metricsParams['aggregator']
    downsample = metricsParams['downsample']
    rate = metricsParams['metric']
    tagKey = metricsParams['tagKey']
    host = metricsParams['host']
    port = metricsParams['port']
    ms = metricsParams['ms']
    arrays = metricsParams['arrays']
    tsuids = metricsParams['tsuids']
    annotations = metricsParams['annotations']
    startDate = metricsParams['startDate']
    endDate = metricsParams['endDate']


    # url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate +  '&m=' + aggregator + ':' + downsample + ':' + metric 

    url = 'http://' + str(host) + ':' + str(port) + '/api/query?' + 'ms=' + ms + '&arrays=' + arrays + '&show_tsuids=' + tsuids + '&global_annotations=' + annotations + '&start=' + startDate + '&end=' + endDate + '&m=' + aggregator + ':' + downsample + ':' + metric

    return url

def purgeRequests(url):
    response = requests.delete(url)
    return response

def purge():
    metrics = loadMetrics()

    for metric in metrics:
        print(metric)
        url = generateURL(metric)
        print(url)
        outputResponse = purgeRequests(url)
    # response = requests.delete(url, data=json.dumps(payload), headers=headers,auth=HTTPBasicAuth(toggl_token, 'api_token'))


    return

purge()


# Just needs to change the opentsdb config file so that the metrics can be deleted from the database using the http query