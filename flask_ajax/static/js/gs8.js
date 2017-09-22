    var gs8 = echarts.init(document.getElementById('gs8'),'macarons');

    // 设置gs8图例
    gs8.setOption({
        title: {
            text: '正在数据加载示例'
        },
        tooltip: {},
        legend: {
            data:['每月发帖量']
        },
        xAxis: {
            data: []
        },
        yAxis: {},
        series: [{
            name: '发帖量',
            type: 'bar',
            data: []
        }]
    })
    gs8.showLoading(); // 显示加载动画
    // 异步加载数据
    $.post('/gs8').done(function (data) {
        gs8.hideLoading(); // 隐藏加载动画

        // 填入数据
        gs8.setOption({
            xAxis: {
                data: data.month
            },
            series: [{
                name: '发帖量', // 根据名字对应到相应的系列
                data: data.nums.map(parseFloat) // 转化为数字（注意map）
            }]
        });
    })