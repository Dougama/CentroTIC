$(document).ready(function(){
    // evento del click del boton con id = hour1

        $.ajax({
            type: "GET",
            url: "/app_sensado/historico-datos-json/",
            data: {},
            dataType: 'json',
            success: function (data){
                   // temperatura
                   Highcharts.chart('grafica_temperatura', {
                    chart: {
                        zoomType: 'x'
                    },
                    title: {
                        text: 'Temperatura °C'
                    },
                    subtitle: {
                        text: document.ontouchstart === undefined ?
                                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
                    },
                    xAxis: {
                        type: 'datetime',
                        
                    },
                    
                    yAxis: {
                        title: {
                            text: 'Temperatura °C'
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    plotOptions: {
                        area: {
                            fillColor: {
                                linearGradient: {
                                    x1: 0,
                                    y1: 0,
                                    x2: 0,
                                    y2: 1
                                },
                                stops: [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                                ]
                            },
                            marker: {
                                radius: 2
                            },
                            lineWidth: 1,
                            states: {
                                hover: {
                                    lineWidth: 1
                                }
                            },
                            threshold: null
                        }
                    },
        
                    time: {
                        timezone: 'America/Bogota'
                    },
                    
                    series: [{
                        type: 'area',
                        name: 'Temperatura',
                        data: data.temperatura,
                            }]
                }); //fin hightcharts


                // humedad
                Highcharts.chart('grafica_humedad', {
                    chart: {
                        zoomType: 'x'
                    },
                    title: {
                        text: 'Huemdad %'
                    },
                    subtitle: {
                        text: document.ontouchstart === undefined ?
                                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
                    },
                    xAxis: {
                        type: 'datetime',
                        
                    },
                    
                    yAxis: {
                        title: {
                            text: 'Humedad'
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    plotOptions: {
                        area: {
                            fillColor: {
                                linearGradient: {
                                    x1: 0,
                                    y1: 0,
                                    x2: 0,
                                    y2: 1
                                },
                                stops: [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                                ]
                            },
                            marker: {
                                radius: 2
                            },
                            lineWidth: 1,
                            states: {
                                hover: {
                                    lineWidth: 1
                                }
                            },
                            threshold: null
                        }
                    },
        
                    time: {
                        timezone: 'America/Bogota'
                    },
                    
                    series: [{
                        type: 'area',
                        name: 'Humedad',
                        data: data.humedad,
                            }]
                }); //fin hightcharts
 

                                // humedad
                Highcharts.chart('grafica_humedad', {
                    chart: {
                        zoomType: 'x'
                    },
                    title: {
                        text: 'Humedad %'
                    },
                    subtitle: {
                        text: document.ontouchstart === undefined ?
                                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
                    },
                    xAxis: {
                        type: 'datetime',
                        
                    },
                    
                    yAxis: {
                        title: {
                            text: 'Humedad'
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    plotOptions: {
                        area: {
                            fillColor: {
                                linearGradient: {
                                    x1: 0,
                                    y1: 0,
                                    x2: 0,
                                    y2: 1
                                },
                                stops: [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                                ]
                            },
                            marker: {
                                radius: 2
                            },
                            lineWidth: 1,
                            states: {
                                hover: {
                                    lineWidth: 1
                                }
                            },
                            threshold: null
                        }
                    },
        
                    time: {
                        timezone: 'America/Bogota'
                    },
                    
                    series: [{
                        type: 'area',
                        name: 'Humedad',
                        data: data.humedad,
                            }]
                }); //fin hightcharts
                // amoniaco
                Highcharts.chart('grafica_amoniaco', {
                    chart: {
                        zoomType: 'x'
                    },
                    title: {
                        text: 'Amoniaco'
                    },
                    subtitle: {
                        text: document.ontouchstart === undefined ?
                                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
                    },
                    xAxis: {
                        type: 'datetime',
                        
                    },
                    
                    yAxis: {
                        title: {
                            text: 'Amoniaco'
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    plotOptions: {
                        area: {
                            fillColor: {
                                linearGradient: {
                                    x1: 0,
                                    y1: 0,
                                    x2: 0,
                                    y2: 1
                                },
                                stops: [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                                ]
                            },
                            marker: {
                                radius: 2
                            },
                            lineWidth: 1,
                            states: {
                                hover: {
                                    lineWidth: 1
                                }
                            },
                            threshold: null
                        }
                    },
        
                    time: {
                        timezone: 'America/Bogota'
                    },
                    
                    series: [{
                        type: 'area',
                        name: 'Humedad',
                        data: data.amoniaco,
                            }]
                }); //fin hightcharts

               // amoniaco
               Highcharts.chart('grafica_alcohol', {
                chart: {
                    zoomType: 'x'
                },
                title: {
                    text: 'Alcohol'
                },
                subtitle: {
                    text: document.ontouchstart === undefined ?
                            'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
                },
                xAxis: {
                    type: 'datetime',
                    
                },
                
                yAxis: {
                    title: {
                        text: 'Alcohol'
                    }
                },
                legend: {
                    enabled: false
                },
                plotOptions: {
                    area: {
                        fillColor: {
                            linearGradient: {
                                x1: 0,
                                y1: 0,
                                x2: 0,
                                y2: 1
                            },
                            stops: [
                                [0, Highcharts.getOptions().colors[0]],
                                [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                            ]
                        },
                        marker: {
                            radius: 2
                        },
                        lineWidth: 1,
                        states: {
                            hover: {
                                lineWidth: 1
                            }
                        },
                        threshold: null
                    }
                },
    
                time: {
                    timezone: 'America/Bogota'
                },
                
                series: [{
                    type: 'area',
                    name: 'Alcohol',
                    data: data.alcohol,
                        }]
            }); //fin hightcharts

               // amoniaco
               Highcharts.chart('grafica_CO', {
                chart: {
                    zoomType: 'x'
                },
                title: {
                    text: 'CO'
                },
                subtitle: {
                    text: document.ontouchstart === undefined ?
                            'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
                },
                xAxis: {
                    type: 'datetime',
                    
                },
                
                yAxis: {
                    title: {
                        text: 'CO'
                    }
                },
                legend: {
                    enabled: false
                },
                plotOptions: {
                    area: {
                        fillColor: {
                            linearGradient: {
                                x1: 0,
                                y1: 0,
                                x2: 0,
                                y2: 1
                            },
                            stops: [
                                [0, Highcharts.getOptions().colors[0]],
                                [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                            ]
                        },
                        marker: {
                            radius: 2
                        },
                        lineWidth: 1,
                        states: {
                            hover: {
                                lineWidth: 1
                            }
                        },
                        threshold: null
                    }
                },
    
                time: {
                    timezone: 'America/Bogota'
                },
                
                series: [{
                    type: 'area',
                    name: 'CO',
                    data: data.CO,
                        }]
            }); //fin hightcharts
            } //fin success
        }); // fin ajax

}); //document ready