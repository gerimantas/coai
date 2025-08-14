import { useState, useEffect, useCallback, useRef } from 'react'

const useUsageAnalytics = (initialPeriod = 7) => {
  const [usageStats, setUsageStats] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [statsPeriod, setStatsPeriod] = useState(initialPeriod)
  const [lastUpdated, setLastUpdated] = useState(null)
  const [autoRefresh, setAutoRefresh] = useState(false)
  
  const intervalRef = useRef(null)
  const abortControllerRef = useRef(null)

  const fetchUsageData = useCallback(async (signal) => {
    try {
      setLoading(true)
      setError(null)
      
      const response = await fetch(`/api/usage/stats?days=${statsPeriod}`, {
        signal
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      setUsageStats(data.stats)
      setLastUpdated(new Date().toISOString())
      
    } catch (error) {
      if (error.name !== 'AbortError') {
        console.error('Error fetching usage stats:', error)
        setError(error.message)
      }
    } finally {
      setLoading(false)
    }
  }, [statsPeriod])

  const refreshData = useCallback(() => {
    // Cancel previous request
    if (abortControllerRef.current) {
      abortControllerRef.current.abort()
    }
    
    // Create new abort controller
    abortControllerRef.current = new AbortController()
    fetchUsageData(abortControllerRef.current.signal)
  }, [fetchUsageData])

  // Effect for initial load and period changes
  useEffect(() => {
    refreshData()
  }, [statsPeriod])

  // Effect for auto-refresh
  useEffect(() => {
    if (autoRefresh) {
      intervalRef.current = setInterval(refreshData, 30000) // 30 seconds
      return () => {
        if (intervalRef.current) {
          clearInterval(intervalRef.current)
        }
      }
    } else {
      if (intervalRef.current) {
        clearInterval(intervalRef.current)
      }
    }
  }, [autoRefresh, refreshData])

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current)
      }
      if (abortControllerRef.current) {
        abortControllerRef.current.abort()
      }
    }
  }, [])

  const exportData = useCallback(async (format) => {
    try {
      const response = await fetch(`/api/usage/export?format=${format}&days=${statsPeriod}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        }
      })
      
      if (!response.ok) {
        throw new Error(`Export failed: ${response.status}`)
      }
      
      if (format === 'csv') {
        const csvData = await response.text()
        const blob = new Blob([csvData], { type: 'text/csv' })
        const url = window.URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = `usage-export-${new Date().toISOString().split('T')[0]}.csv`
        document.body.appendChild(a)
        a.click()
        window.URL.revokeObjectURL(url)
        document.body.removeChild(a)
      } else {
        const data = await response.json()
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })
        const url = window.URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = `usage-export-${new Date().toISOString().split('T')[0]}.json`
        document.body.appendChild(a)
        a.click()
        window.URL.revokeObjectURL(url)
        document.body.removeChild(a)
      }
    } catch (error) {
      console.error('Error exporting data:', error)
      setError(`Export failed: ${error.message}`)
    }
  }, [statsPeriod])

  const changePeriod = useCallback((newPeriod) => {
    setStatsPeriod(newPeriod)
  }, [])

  return {
    usageStats,
    loading,
    error,
    statsPeriod,
    lastUpdated,
    autoRefresh,
    setAutoRefresh,
    refreshData,
    exportData,
    changePeriod
  }
}

export default useUsageAnalytics
