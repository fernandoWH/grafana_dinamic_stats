
data_dashboard = {
            "dashboard": {
            "id": None,
            "panels": [
              {
                "aliasColors": {},
                "bars": False,
                "dashLength": 10,
                "dashes": False,
                "datasource": "$empresa",
                "fieldConfig": {
                  "defaults": {
                    "custom": {}
                  },
                  "overrides": []
                },
                "fill": 1,
                "fillGradient": 0,
                "gridPos": {
                  "h": 8,
                  "w": 12,
                  "x": 0,
                  "y": 0
                },
                "hiddenSeries": False,
                "id": 4,
                "legend": {
                  "avg": False,
                  "current": False,
                  "max": False,
                  "min": False,
                  "show": True,
                  "total": False,
                  "values": False
                },
                "lines": True,
                "linewidth": 1,
                "nullPointMode": "null",
                "options": {
                  "alertThreshold": True
                },
                "percentage": False,
                "pluginVersion": "7.2.0-pre",
                "pointradius": 2,
                "points": False,
                "renderer": "flot",
                "seriesOverrides": [],
                "spaceLength": 10,
                "stack": False,
                "steppedLine": False,
                "targets": [
                  {
                    "groupBy": [
                      {
                        "params": [
                          "10s"
                        ],
                        "type": "time"
                      },
                      {
                        "params": [
                          "null"
                        ],
                        "type": "fill"
                      }
                    ],
                    "measurement": "mem",
                    "orderByTime": "ASC",
                    "policy": "default",
                    "refId": "A",
                    "resultFormat": "time_series",
                    "select": [
                      [
                        {
                          "params": [
                            "used"
                          ],
                          "type": "field"
                        },
                        {
                          "params": [],
                          "type": "mean"
                        }
                      ]
                    ],
                    "tags": [
                      {
                        "key": "host",
                        "operator": "=~",
                        "value": "/^$servidor$/"
                      }
                    ]
                  }
                ],
                "thresholds": [],
                "timeFrom": None,
                "timeRegions": [],
                "timeShift": None,
                "title": "RAM",
                "tooltip": {
                  "shared": True,
                  "sort": 0,
                  "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                  "buckets": None,
                  "mode": "time",
                  "name": None,
                  "show": True,
                  "values": []
                },
                "yaxes": [
                  {
                    "format": "decbytes",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  },
                  {
                    "format": "short",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  }
                ],
                "yaxis": {
                  "align": False,
                  "alignLevel": None
                }
              },
              {
                "aliasColors": {},
                "bars": False,
                "dashLength": 10,
                "dashes": False,
                "datasource": "$empresa",
                "fieldConfig": {
                  "defaults": {
                    "custom": {}
                  },
                  "overrides": []
                },
                "fill": 1,
                "fillGradient": 0,
                "gridPos": {
                  "h": 8,
                  "w": 12,
                  "x": 12,
                  "y": 0
                },
                "hiddenSeries": False,
                "id": 6,
                "legend": {
                  "avg": False,
                  "current": False,
                  "max": False,
                  "min": False,
                  "show": True,
                  "total": False,
                  "values": False
                },
                "lines": True,
                "linewidth": 1,
                "nullPointMode": "null",
                "options": {
                  "alertThreshold": True
                },
                "percentage": False,
                "pluginVersion": "7.2.0-pre",
                "pointradius": 2,
                "points": False,
                "renderer": "flot",
                "seriesOverrides": [],
                "spaceLength": 10,
                "stack": False,
                "steppedLine": False,
                "targets": [
                  {
                    "groupBy": [
                      {
                        "params": [
                          "10s"
                        ],
                        "type": "time"
                      },
                      {
                        "params": [
                          "null"
                        ],
                        "type": "fill"
                      }
                    ],
                    "measurement": "net",
                    "orderByTime": "ASC",
                    "policy": "default",
                    "refId": "A",
                    "resultFormat": "time_series",
                    "select": [
                      [
                        {
                          "params": [
                            "bytes_recv"
                          ],
                          "type": "field"
                        },
                        {
                          "params": [],
                          "type": "mean"
                        },
                        {
                          "params": [
                            "1s"
                          ],
                          "type": "non_negative_derivative"
                        },
                        {
                          "params": [
                            "*8"
                          ],
                          "type": "math"
                        }
                      ]
                    ],
                    "tags": [
                      {
                        "key": "host",
                        "operator": "=~",
                        "value": "/^$servidor$/"
                      }
                    ]
                  },
                  {
                    "groupBy": [
                      {
                        "params": [
                          "10s"
                        ],
                        "type": "time"
                      },
                      {
                        "params": [
                          "null"
                        ],
                        "type": "fill"
                      }
                    ],
                    "measurement": "net",
                    "orderByTime": "ASC",
                    "policy": "default",
                    "refId": "B",
                    "resultFormat": "time_series",
                    "select": [
                      [
                        {
                          "params": [
                            "bytes_sent"
                          ],
                          "type": "field"
                        },
                        {
                          "params": [],
                          "type": "mean"
                        },
                        {
                          "params": [
                            "1s"
                          ],
                          "type": "non_negative_derivative"
                        },
                        {
                          "params": [
                            "*8"
                          ],
                          "type": "math"
                        }
                      ]
                    ],
                    "tags": [
                      {
                        "key": "host",
                        "operator": "=~",
                        "value": "/^$servidor$/"
                      }
                    ]
                  }
                ],
                "thresholds": [],
                "timeFrom": None,
                "timeRegions": [],
                "timeShift": None,
                "title": "BandWidth",
                "tooltip": {
                  "shared": True,
                  "sort": 0,
                  "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                  "buckets": None,
                  "mode": "time",
                  "name": None,
                  "show": True,
                  "values": []
                },
                "yaxes": [
                  {
                    "format": "Bps",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  },
                  {
                    "format": "short",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  }
                ],
                "yaxis": {
                  "align": False,
                  "alignLevel": None
                }
              },
              {
                "aliasColors": {},
                "bars": False,
                "dashLength": 10,
                "dashes": False,
                "datasource": "$empresa",
                "fieldConfig": {
                  "defaults": {
                    "custom": {}
                  },
                  "overrides": []
                },
                "fill": 1,
                "fillGradient": 0,
                "gridPos": {
                  "h": 8,
                  "w": 12,
                  "x": 0,
                  "y": 8
                },
                "hiddenSeries": False,
                "id": 2,
                "legend": {
                  "avg": False,
                  "current": False,
                  "max": False,
                  "min": False,
                  "show": True,
                  "total": False,
                  "values": False
                },
                "lines": True,
                "linewidth": 1,
                "nullPointMode": "null",
                "options": {
                  "alertThreshold": True
                },
                "percentage": False,
                "pluginVersion": "7.2.0-pre",
                "pointradius": 2,
                "points": False,
                "renderer": "flot",
                "seriesOverrides": [],
                "spaceLength": 10,
                "stack": False,
                "steppedLine": False,
                "targets": [
                  {
                    "groupBy": [
                      {
                        "params": [
                          "10s"
                        ],
                        "type": "time"
                      },
                      {
                        "params": [
                          "null"
                        ],
                        "type": "fill"
                      }
                    ],
                    "measurement": "cpu",
                    "orderByTime": "ASC",
                    "policy": "default",
                    "refId": "A",
                    "resultFormat": "time_series",
                    "select": [
                      [
                        {
                          "params": [
                            "usage_system"
                          ],
                          "type": "field"
                        },
                        {
                          "params": [],
                          "type": "mean"
                        }
                      ]
                    ],
                    "tags": [
                      {
                        "key": "host",
                        "operator": "=~",
                        "value": "/^$servidor$/"
                      }
                    ]
                  }
                ],
                "thresholds": [],
                "timeFrom": None,
                "timeRegions": [],
                "timeShift": None,
                "title": "CPU",
                "tooltip": {
                  "shared": True,
                  "sort": 0,
                  "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                  "buckets": None,
                  "mode": "time",
                  "name": None,
                  "show": True,
                  "values": []
                },
                "yaxes": [
                  {
                    "format": "short",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  },
                  {
                    "format": "short",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  }
                ],
                "yaxis": {
                  "align": False,
                  "alignLevel": None
                }
              },
              {
                "aliasColors": {},
                "bars": False,
                "dashLength": 10,
                "dashes": False,
                "datasource": "$empresa",
                "fieldConfig": {
                  "defaults": {
                    "custom": {}
                  },
                  "overrides": []
                },
                "fill": 1,
                "fillGradient": 0,
                "gridPos": {
                  "h": 8,
                  "w": 12,
                  "x": 12,
                  "y": 8
                },
                "hiddenSeries": False,
                "id": 8,
                "legend": {
                  "avg": False,
                  "current": False,
                  "max": False,
                  "min": False,
                  "show": True,
                  "total": False,
                  "values": False
                },
                "lines": True,
                "linewidth": 1,
                "nullPointMode": "null",
                "options": {
                  "alertThreshold": True
                },
                "percentage": False,
                "pluginVersion": "7.2.0-pre",
                "pointradius": 2,
                "points": False,
                "renderer": "flot",
                "seriesOverrides": [],
                "spaceLength": 10,
                "stack": False,
                "steppedLine": False,
                "targets": [
                  {
                    "groupBy": [
                      {
                        "params": [
                          "10s"
                        ],
                        "type": "time"
                      },
                      {
                        "params": [
                          "null"
                        ],
                        "type": "fill"
                      }
                    ],
                    "measurement": "net",
                    "orderByTime": "ASC",
                    "policy": "default",
                    "refId": "A",
                    "resultFormat": "time_series",
                    "select": [
                      [
                        {
                          "params": [
                            "bytes_recv"
                          ],
                          "type": "field"
                        },
                        {
                          "params": [],
                          "type": "mean"
                        },
                        {
                          "params": [],
                          "type": "non_negative_difference"
                        }
                      ]
                    ],
                    "tags": [
                      {
                        "key": "host",
                        "operator": "=~",
                        "value": "/^$servidor$/"
                      }
                    ]
                  }
                ],
                "thresholds": [],
                "timeFrom": None,
                "timeRegions": [],
                "timeShift": None,
                "title": "Download",
                "tooltip": {
                  "shared": True,
                  "sort": 0,
                  "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                  "buckets": None,
                  "mode": "time",
                  "name": None,
                  "show": True,
                  "values": []
                },
                "yaxes": [
                  {
                    "format": "decbytes",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  },
                  {
                    "format": "short",
                    "label": None,
                    "logBase": 1,
                    "max": None,
                    "min": None,
                    "show": True
                  }
                ],
                "yaxis": {
                  "align": False,
                  "alignLevel": None
                }
              }
            ],
            "tags": [],
            "templating": {
              "list": [
                {
                  "allFormat": "glob",
                  "current": {
                    "selected": False,
                    "text": "00000000000001",
                    "value": "00000000000001"
                  },
                  "datasource": None,
                  "hide": 2,
                  "includeAll": False,
                  "label": None,
                  "multi": False,
                  "name": "empresa",
                  "options": [],
                  "query": "influxdb",
                  "refresh": 1,
                  "regex": "",
                  "skipUrlSync": False,
                  "type": "datasource"
                },
                {
                  "allValue": None,
                  "current": {
                    "selected": False,
                    "text": "sin-conexion",
                    "value": "sin-conexion"
                  },
                  "datasource": "$empresa",
                  "definition": "SHOW TAG VALUES WITH KEY=\"host\"",
                  "hide": 0,
                  "includeAll": False,
                  "label": "Servidor",
                  "multi": False,
                  "name": "servidor",
                  "options": [],
                  "query": "SHOW TAG VALUES WITH KEY=\"host\"",
                  "refresh": 1,
                  "regex": "",
                  "skipUrlSync": False,
                  "sort": 0,
                  "tagValuesQuery": "",
                  "tags": [],
                  "tagsQuery": "",
                  "type": "query",
                  "useTags": False
                }
              ]
            },
            "time": {
              "from": "now-1h",
              "to": "now"
            },
            "timepicker": {
              "refresh_intervals": [
                "5s",
                "10s",
                "30s",
                "1m",
                "5m",
                "15m",
                "30m",
                "1h",
                "2h",
                "1d"
              ]
            },
            "timezone": "",
            "title": "Server Status",
            "uid": None,
            "version": 1
          }
            }