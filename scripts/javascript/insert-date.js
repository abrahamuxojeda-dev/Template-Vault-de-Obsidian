/**
 * insert-date.js
 * Templater script for date and time utilities
 * 
 * Usage in templates:
 * <% tp.user.insert_date() %>
 * <% tp.user.insert_date("custom", "DD/MM/YYYY") %>
 * <% tp.user.insert_date("week_start") %>
 */

function insert_date(format = "default", customFormat = null) {
    const moment = window.moment;
    const now = moment();
    
    const formats = {
        // Basic formats
        "default": now.format("YYYY-MM-DD"),
        "long": now.format("dddd, MMMM DD, YYYY"),
        "short": now.format("MM/DD/YYYY"),
        "time": now.format("HH:mm"),
        "datetime": now.format("YYYY-MM-DD HH:mm"),
        "timestamp": now.format("YYYY-MM-DD HH:mm:ss"),
        
        // ISO formats
        "iso": now.toISOString(),
        "iso_date": now.format("YYYY-MM-DD"),
        
        // Relative dates
        "yesterday": now.subtract(1, 'days').format("YYYY-MM-DD"),
        "tomorrow": now.add(1, 'days').format("YYYY-MM-DD"),
        "week_start": now.startOf('week').format("YYYY-MM-DD"),
        "week_end": now.endOf('week').format("YYYY-MM-DD"),
        "month_start": now.startOf('month').format("YYYY-MM-DD"),
        "month_end": now.endOf('month').format("YYYY-MM-DD"),
        
        // Week/Month/Quarter
        "week": now.format("YYYY-[W]WW"),
        "month": now.format("YYYY-MM"),
        "quarter": now.format("YYYY-[Q]Q"),
        "year": now.format("YYYY"),
        
        // Natural language
        "day_name": now.format("dddd"),
        "month_name": now.format("MMMM"),
        "month_year": now.format("MMMM YYYY"),
        
        // Unix
        "unix": now.unix().toString(),
        "unix_ms": now.valueOf().toString(),
    };
    
    if (customFormat) {
        return now.format(customFormat);
    }
    
    return formats[format] || formats["default"];
}

function get_week_dates() {
    const moment = window.moment;
    const startOfWeek = moment().startOf('week');
    const dates = [];
    
    for (let i = 0; i < 7; i++) {
        dates.push({
            date: startOfWeek.clone().add(i, 'days').format("YYYY-MM-DD"),
            day: startOfWeek.clone().add(i, 'days').format("dddd"),
            short: startOfWeek.clone().add(i, 'days').format("ddd"),
        });
    }
    
    return dates;
}

function get_month_dates() {
    const moment = window.moment;
    const startOfMonth = moment().startOf('month');
    const daysInMonth = moment().daysInMonth();
    const dates = [];
    
    for (let i = 0; i < daysInMonth; i++) {
        dates.push({
            date: startOfMonth.clone().add(i, 'days').format("YYYY-MM-DD"),
            day: startOfMonth.clone().add(i, 'days').format("DD"),
            weekday: startOfMonth.clone().add(i, 'days').format("ddd"),
        });
    }
    
    return dates;
}

function days_until(targetDate) {
    const moment = window.moment;
    const target = moment(targetDate);
    const now = moment();
    return target.diff(now, 'days');
}

function days_since(pastDate) {
    const moment = window.moment;
    const past = moment(pastDate);
    const now = moment();
    return now.diff(past, 'days');
}

function format_duration(minutes) {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    
    if (hours === 0) return `${mins}m`;
    if (mins === 0) return `${hours}h`;
    return `${hours}h ${mins}m`;
}

function get_time_block(hour = null) {
    const currentHour = hour || new Date().getHours();
    
    if (currentHour < 6) return "night";
    if (currentHour < 12) return "morning";
    if (currentHour < 18) return "afternoon";
    return "evening";
}

function get_quarter_info() {
    const moment = window.moment;
    const now = moment();
    const quarter = now.quarter();
    const year = now.year();
    
    return {
        quarter: quarter,
        year: year,
        formatted: `Q${quarter} ${year}`,
        start: now.startOf('quarter').format("YYYY-MM-DD"),
        end: now.endOf('quarter').format("YYYY-MM-DD"),
    };
}

function get_fiscal_year(fiscalStart = 4) {
    // fiscalStart: month when fiscal year starts (1-12)
    const moment = window.moment;
    const now = moment();
    const currentMonth = now.month() + 1; // moment months are 0-indexed
    
    if (currentMonth >= fiscalStart) {
        return now.year();
    } else {
        return now.year() - 1;
    }
}

function working_days_between(startDate, endDate) {
    const moment = window.moment;
    let start = moment(startDate);
    const end = moment(endDate);
    let workingDays = 0;
    
    while (start <= end) {
        const dayOfWeek = start.day();
        if (dayOfWeek !== 0 && dayOfWeek !== 6) { // Not Sunday or Saturday
            workingDays++;
        }
        start.add(1, 'days');
    }
    
    return workingDays;
}

function get_week_number() {
    const moment = window.moment;
    return moment().format("WW");
}

function is_weekend() {
    const moment = window.moment;
    const day = moment().day();
    return day === 0 || day === 6;
}

function next_weekday(targetDay) {
    // targetDay: 0 = Sunday, 1 = Monday, etc.
    const moment = window.moment;
    const now = moment();
    const currentDay = now.day();
    
    let daysToAdd = targetDay - currentDay;
    if (daysToAdd <= 0) {
        daysToAdd += 7;
    }
    
    return now.add(daysToAdd, 'days').format("YYYY-MM-DD");
}

function last_weekday(targetDay) {
    const moment = window.moment;
    const now = moment();
    const currentDay = now.day();
    
    let daysToSubtract = currentDay - targetDay;
    if (daysToSubtract <= 0) {
        daysToSubtract += 7;
    }
    
    return now.subtract(daysToSubtract, 'days').format("YYYY-MM-DD");
}

// Export all functions
module.exports = {
    insert_date,
    get_week_dates,
    get_month_dates,
    days_until,
    days_since,
    format_duration,
    get_time_block,
    get_quarter_info,
    get_fiscal_year,
    working_days_between,
    get_week_number,
    is_weekend,
    next_weekday,
    last_weekday
};