import React from 'react'

// Simple CSS-based charts for compatibility
export const UsageChart = ({ data, type = 'line', title }) => {
  if (!data || data.length === 0) {
    return (
      <div className="h-64 w-full flex items-center justify-center bg-gray-50 rounded-lg">
        <div className="text-center">
          <div className="text-gray-400 text-sm">{title}</div>
          <div className="text-gray-500 text-xs mt-1">No data available</div>
        </div>
      </div>
    )
  }

  if (type === 'line') {
    const maxValue = Math.max(...data.map(d => d.requests || 0))
    
    return (
      <div className="h-64 w-full">
        <h3 className="text-sm font-medium mb-2">{title}</h3>
        <div className="h-48 bg-gray-50 rounded-lg p-4 relative border">
          <div className="flex items-end justify-between h-full space-x-1">
            {data.slice(-7).map((item, index) => {
              const height = maxValue > 0 ? (item.requests / maxValue) * 100 : 5
              return (
                <div key={index} className="flex flex-col items-center flex-1 group">
                  <div 
                    className="bg-blue-500 rounded-t min-h-[4px] w-full transition-all duration-500 hover:bg-blue-600 group-hover:shadow-lg"
                    style={{ height: `${Math.max(height, 5)}%` }}
                    title={`${item.date}: ${item.requests} requests`}
                  ></div>
                  <div className="text-xs text-gray-500 mt-1 transform -rotate-45 origin-left">
                    {item.date?.split('-').slice(1).join('/')}
                  </div>
                  <div className="text-xs font-medium text-gray-700 mt-1 opacity-0 group-hover:opacity-100 transition-opacity">
                    {item.requests}
                  </div>
                </div>
              )
            })}
          </div>
          <div className="absolute top-2 right-2 text-xs text-gray-400">
            Max: {maxValue}
          </div>
        </div>
      </div>
    )
  }

  if (type === 'pie') {
    const total = data.reduce((sum, item) => sum + item.value, 0)
    const colors = ['bg-blue-500', 'bg-green-500', 'bg-yellow-500', 'bg-red-500', 'bg-purple-500', 'bg-indigo-500']
    
    return (
      <div className="h-64 w-full">
        <h3 className="text-sm font-medium mb-2">{title}</h3>
        <div className="flex items-center justify-center h-48 space-x-6">
          
          {/* Simple pie chart representation */}
          <div className="relative">
            <div className="w-24 h-24 rounded-full border-8 border-gray-200 relative overflow-hidden">
              {data.map((item, index) => {
                const percentage = ((item.value / total) * 100).toFixed(1)
                return (
                  <div
                    key={index}
                    className={`absolute inset-0 ${colors[index % colors.length]} opacity-80`}
                    style={{
                      clipPath: `polygon(50% 50%, 50% 0%, ${50 + (item.value / total) * 50}% 0%, 50% 50%)`
                    }}
                    title={`${item.name}: ${percentage}%`}
                  />
                )
              })}
            </div>
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center text-xs font-bold">
                {data.length}
              </div>
            </div>
          </div>

          {/* Legend */}
          <div className="space-y-2">
            {data.map((item, index) => {
              const percentage = ((item.value / total) * 100).toFixed(1)
              return (
                <div key={index} className="flex items-center text-sm group hover:bg-gray-50 p-1 rounded">
                  <div className={`w-3 h-3 ${colors[index % colors.length]} rounded mr-2 group-hover:scale-110 transition-transform`}></div>
                  <span className="flex-1">{item.name}</span>
                  <span className="font-medium ml-2">{percentage}%</span>
                  <span className="text-gray-500 ml-1">({item.value})</span>
                </div>
              )
            })}
          </div>
        </div>
      </div>
    )
  }

  if (type === 'bar') {
    const maxValue = Math.max(...data.map(d => d.value || 0))
    
    return (
      <div className="h-64 w-full">
        <h3 className="text-sm font-medium mb-2">{title}</h3>
        <div className="h-48 bg-gray-50 rounded-lg p-4 space-y-2">
          {data.slice(0, 6).map((item, index) => {
            const width = maxValue > 0 ? (item.value / maxValue) * 100 : 0
            return (
              <div key={index} className="flex items-center space-x-3">
                <div className="w-20 text-sm text-gray-600 truncate">{item.name}</div>
                <div className="flex-1 bg-gray-200 rounded-full h-4 relative">
                  <div 
                    className="bg-green-500 h-4 rounded-full transition-all duration-500 hover:bg-green-600"
                    style={{ width: `${width}%` }}
                    title={`${item.name}: ${item.value}`}
                  ></div>
                </div>
                <div className="w-12 text-sm font-medium text-gray-700">{item.value}</div>
              </div>
            )
          })}
        </div>
      </div>
    )
  }

  return null
}
