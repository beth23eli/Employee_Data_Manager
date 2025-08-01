import React, { useState } from "react";
import './style.css';



function Dashboard() {
    const [resultMsg, setResultMsg] = useState("");
    const [archiveMsg, setArchiveMsg] = useState("");


    async function generateExcel() {
        setArchiveMsg("")
        try {
            const response = await fetch(
                "http://127.0.0.1:5000/employees/operations/generation/createAggregatedEmployeeData",
                {
                    method: "POST",
                }
            );
            if (!response.ok) throw new Error("Excel generation failed");
            const data = await response.json();
            console.log("Excel:", data);
            setResultMsg(data.message || "Excel generated successfully.");
        } catch (error) {
            console.error("Fetch error:", error);
            setResultMsg(error.message);
        }
    }

    async function generatePdfs() {
        try {
            const response = await fetch(
                "http://127.0.0.1:5000/employees/operations/generation/createPdfForEmployees",
                {
                    method: "POST",
                }
            );
            if (!response.ok) throw new Error("PDF generation failed");
            const data = await response.json();
            console.log("PDFs:", data);
            setResultMsg(data.message || "PDFs generated successfully.");
        } catch (error) {
            console.error("Fetch error:", error);
            setResultMsg(error.message);
        }
    }

    async function sendFiles() {
        setResultMsg("Sending reports...");

        try {
            // send to manager
            const sendExcelRes = await fetch(
                "http://127.0.0.1:5000/employees/operations/sending/sendAggregatedEmployeeData",
                {
                    method: "POST",
                }
            );
            if (!sendExcelRes.ok) throw new Error("Failed to send Excel to manager");
            await sendExcelRes.json();

            setResultMsg("Excel sent to manager. Sending PDFs to employees...");

            // send to employees
            const sendPdfsRes = await fetch(
                "http://127.0.0.1:5000/employees/operations/sending/sendPdfToEmployees",
                {
                    method: "POST",
                }
            );
            if (!sendPdfsRes.ok) throw new Error("Failed to send PDFs to employees");
            await sendPdfsRes.json();
            setResultMsg("All reports sent successfully.");

            setArchiveMsg("Creating the archive...");
            // create archive when sending is complete
            const createArchRes = await fetch(
                "http://127.0.0.1:5000/employees/operations/generation/createArchive",
                {
                    method: "POST",
                }
            );
            if (!createArchRes.ok) throw new Error("Failed to create the archive");
            await createArchRes.json();
            setArchiveMsg("The archive with all the files was created.");

        } catch (error) {
            console.error("Error in createArchive:", error);
            setResultMsg(error.message);
        }
    }

    return (
        <div className="mainArea">
            <h2>Employee salary report generation</h2>

            <div className="mainArea__generateBtns">
                <button onClick={generateExcel}>Generate Employee Summary</button>
                <button onClick={generatePdfs}>Generate Employee Salary Report</button>
            </div>

            <div className="mainArea__sendBtns">
                <button onClick={sendFiles}>Send Monthly Reports</button>
            </div>

            <div className="mainArea__messages">
                {resultMsg} <br />
                {archiveMsg}
            </div>
        </div>
    );
}

export default Dashboard;
