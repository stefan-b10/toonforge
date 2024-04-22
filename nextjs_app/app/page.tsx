"use client";

import { useState } from "react";
import InputSection from "@/components/InputSection";
import { Card, Col, Row, Button } from "antd";
import Image from "next/image";

export default function Home() {
	const [description, setDescription] = useState("");
	const [negativeDescription, setNegativeDescription] = useState("");

	return (
		<div className="bg-gray-900 min-h-screen text-white">
			<div>
				<Row>
					<Col span={14}></Col>
					<Col span={10}>
						<Card
							size="small"
							title={
								<span className="text-white font-bold text-lg">Input</span>
							}
							className="bg-neutral-900 m-2 text-white border-green-400	"
						>
							<InputSection
								title="Description:"
								placeholder="a superhero at a job interview"
								data={description}
								setData={setDescription}
							/>
							<InputSection
								title="Negative Description (optional):"
								placeholder="things you DON'T want in the comics"
								data={negativeDescription}
								setData={setNegativeDescription}
							/>
							<Button
								type="primary"
								className="bg-green-800 size-full rounded-md text-xl"
							>
								Generate
							</Button>
						</Card>
					</Col>
				</Row>
				{/* LEFT COLUMN */}
				<div></div>
				{/* RUGHT COLUMN */}
				{/* <div>
					<InputSection
						title="Description"
						placeholder="a superhero at a job interview"
						data={description}
						setData={setDescription}
					/>
					<InputSection
						title="Negative Description"
						placeholder="things you DON'T want in the comics"
						data={negativeDescription}
						setData={setNegativeDescription}
					/>
				</div> */}
			</div>
		</div>
	);
}
