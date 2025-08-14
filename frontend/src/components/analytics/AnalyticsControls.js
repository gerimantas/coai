import { useState } from 'react'
import { Button } from "@/components/ui/Button"
import { Badge } from "@/components/ui/Badge"
// Temporarily remove lucide-react imports due to React 19 compatibility
// import { Calendar, Filter, Download, RefreshCw, TrendingUp, TrendingDown } from 'lucide-react'

export const AnalyticsControls = ({ 
  statsPeriod, 
  setStatsPeriod, 
  onRefresh, 
  onExport, 
  isLoading,
  lastUpdated,
  autoRefresh,
  setAutoRefresh 
}) => {
  const [filterOpen, setFilterOpen] = useState(false)

  return (
    <div className="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
      
      {/* Period Selection */}
      <div className="flex flex-wrap gap-2">
        {[7, 14, 30, 90].map((days) => (
          <Button
            key={days}
            variant={statsPeriod === days ? "default" : "outline"}
            onClick={() => setStatsPeriod(days)}
            size="sm"
            className="relative"
          >
            Last {days} days
            {statsPeriod === days && (
              <div className="absolute -top-1 -right-1 w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
            )}
          </Button>
        ))}
        
        {/* Custom Date Range */}
        <Button
          variant="outline"
          size="sm"
          onClick={() => setFilterOpen(!filterOpen)}
          className="flex items-center gap-2"
        >
          <span>📅</span>
          Custom
        </Button>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap gap-2 items-center">
        
        {/* Auto Refresh Toggle */}
        <Button
          variant={autoRefresh ? "default" : "outline"}
          size="sm"
          onClick={() => setAutoRefresh(!autoRefresh)}
          className="flex items-center gap-2"
        >
          <div className={`w-2 h-2 rounded-full ${autoRefresh ? 'bg-green-400 animate-pulse' : 'bg-gray-400'}`}></div>
          Auto
        </Button>

        {/* Manual Refresh */}
        <Button
          variant="outline"
          size="sm"
          onClick={onRefresh}
          disabled={isLoading}
          className="flex items-center gap-2"
        >
          <span className={isLoading ? 'animate-spin' : ''}>🔄</span>
          Refresh
        </Button>

        {/* Export Options */}
        <div className="flex gap-1">
          <Button 
            onClick={() => onExport('json')} 
            variant="outline" 
            size="sm"
            className="flex items-center gap-2"
          >
            <span>📄</span>
            JSON
          </Button>
          <Button 
            onClick={() => onExport('csv')} 
            variant="outline" 
            size="sm"
            className="flex items-center gap-2"
          >
            <span>📊</span>
            CSV
          </Button>
        </div>
      </div>

      {/* Last Updated Info */}
      {lastUpdated && (
        <div className="text-xs text-gray-500 flex items-center gap-2">
          <div className="w-2 h-2 bg-green-400 rounded-full"></div>
          Last updated: {new Date(lastUpdated).toLocaleTimeString()}
        </div>
      )}
    </div>
  )
}

export const MetricTrend = ({ value, previousValue, label, format = 'number' }) => {
  const change = previousValue ? ((value - previousValue) / previousValue) * 100 : 0
  const isPositive = change > 0
  const isNegative = change < 0
  
  const formatValue = (val) => {
    if (format === 'currency') return `$${val.toFixed(4)}`
    if (format === 'percentage') return `${val.toFixed(1)}%`
    if (format === 'time') return `${val.toFixed(2)}s`
    return val.toLocaleString()
  }
  
  return (
    <div className="flex items-center gap-2">
      <span className="text-2xl font-bold">{formatValue(value)}</span>
      {previousValue && (
        <div className={`flex items-center gap-1 text-sm ${
          isPositive ? 'text-green-600' : isNegative ? 'text-red-600' : 'text-gray-500'
        }`}>
          {isPositive && <span>📈</span>}
          {isNegative && <span>📉</span>}
          <span>{Math.abs(change).toFixed(1)}%</span>
        </div>
      )}
    </div>
  )
}
